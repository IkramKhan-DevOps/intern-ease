var notify_badge_class;
var notify_menu_class;
var notify_api_url;
var notify_fetch_count;
var notify_unread_url;
var notify_mark_all_unread_url;
var notify_refresh_period = 15000;
var consecutive_misfires = 0;
var registered_functions = [];

function fill_notification_badge(data) {
    var badges = document.getElementsByClassName(notify_badge_class);
    if (badges) {
        for (var i = 0; i < badges.length; i++) {
            badges[i].innerHTML = data.unread_count;
        }
    }
}

function my_special_notification_callback(data) {
    let x = '';
    for (var i = 0; i < data.unread_list.length; i++) {
        content = data.unread_list[i];

        x += `<a href="" class="text-reset notification-item">
                            <div class="media">
                              
                                <div class="media-body">
                                    <h6 class="mt-0 mb-1">${content.verb}</h6>
                                    <div class="font-size-12 text-muted">
                                        <p class="mb-1 font-size-11">${content.description}</p>
                                        <p class="mb-0"><i class="mdi mdi-clock-outline"></i> ${timeSince(new Date(content.timestamp))} ago</p>
                                    </div>
                                </div>
                            </div>
                        </a>`;
    }
    $('#notify_me_now').html(x)
}

function fill_notification_list(data) {
    var menus = document.getElementsByClassName(notify_menu_class);
    if (menus) {
        var messages = data.unread_list.map(function (item) {
            var message = "";
            if (typeof item.actor !== 'undefined') {
                message = item.actor;
            }
            if (typeof item.verb !== 'undefined') {
                message = message + " " + item.verb;
            }
            if (typeof item.target !== 'undefined') {
                message = message + " " + item.target;
            }
            if (typeof item.timestamp !== 'undefined') {
                message = message + " " + item.timestamp;
            }
            return '<li>' + message + '</li>';
        }).join('')

        for (var i = 0; i < menus.length; i++) {
            menus[i].innerHTML = messages;
        }
    }
}

function register_notifier(func) {
    registered_functions.push(func);
}

function fetch_api_data() {
    if (registered_functions.length > 0) {
        //only fetch data if a function is setup
        var r = new XMLHttpRequest();
        r.addEventListener('readystatechange', function (event) {
            if (this.readyState === 4) {
                if (this.status === 200) {
                    consecutive_misfires = 0;
                    var data = JSON.parse(r.responseText);
                    registered_functions.forEach(function (func) {
                        func(data);
                    });
                } else {
                    consecutive_misfires++;
                }
            }
        })
        r.open("GET", notify_api_url + '?max=' + notify_fetch_count, true);
        r.send();
    }
    if (consecutive_misfires < 10) {
        setTimeout(fetch_api_data, notify_refresh_period);
    } else {
        var badges = document.getElementsByClassName(notify_badge_class);
        if (badges) {
            for (var i = 0; i < badges.length; i++) {
                badges[i].innerHTML = "!";
                badges[i].title = "Connection lost!"
            }
        }
    }
}

function timeSince(date) {

    var seconds = Math.floor((new Date() - date) / 1000);

    var interval = Math.floor(seconds / 31536000);

    if (interval > 1) {
        return interval + " years";
    }
    interval = Math.floor(seconds / 2592000);
    if (interval > 1) {
        return interval + " months";
    }
    interval = Math.floor(seconds / 86400);
    if (interval > 1) {
        return interval + " days";
    }
    interval = Math.floor(seconds / 3600);
    if (interval > 1) {
        return interval + " hours";
    }
    interval = Math.floor(seconds / 60);
    if (interval > 1) {
        return interval + " minutes";
    }
    return Math.floor(seconds) + " seconds";
}

setTimeout(fetch_api_data, 1000);

function timestampToString(timestamp, useMilliseconds) {
    const periods = {
        day: 86400000,
        hour: 3600000,
        minute: 60000,
        second: 1000,
        millisecond: 1,
    };

    if (!useMilliseconds) {
        timestamp *= 1000;
        delete periods.millisecond;
    }

    return Object.entries(periods)
        .reduce((result, [period, value]) => {
            const num = Math.floor(timestamp / value);
            const plural = num === 1 ? '' : 's';
            const str = `${num} ${period}${plural} `;

            timestamp -= num * value;

            return `${result}${num === 0 ? '' : str}`;
        }, '')
        .trim();
}

function unread_all_notifications() {

    $.get('/inbox/notifications/mark-all-as-read/ ', function (data, status) {
        location.reload();
    });
}