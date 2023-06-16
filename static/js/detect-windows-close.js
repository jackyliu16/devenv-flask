$(window).on('beforeunload', function() {
    // 发送 AJAX 请求
    $.ajax({
        url: '/logout',
        type: 'POST',
        data: {key: 'value'},
        async: false
    });
});