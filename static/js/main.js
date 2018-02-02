$(document).ready(function () {
    $('#typeahead-input').typeahead({
        source: function (query, process) {
            return $.get('/api/blogpost/?format=json&title=' + query, function (data) {
                return process(data);
            });
        },
        updater: function (item) {
            return item;
        },
        displayText: function (item) {
            return item.title;
        },
        afterSelect: function (item) {
            location.href = 'http://localhost:8000/blog/' + item.slug + ".html";
        },
        delay: 500
    });
});

//$(document).ready()方法可以是在DOM完成加载后，运行其中的函数。接着我们开始监听#typeahead-input，
// 对应的便是id为typeahead-input的元素。可以看到在这其中有五个对象：
// source，即搜索的来源，我们返回的是我们搜索的URL。
// updater，即每次更新要做的事
// displayText，显示在页面上的内容，如在这里我们返回的是博客的标题
// afterSelect，每用户选中某一项后做的事，这里我们直接中转到对应的博客。
// delay，延时500ms。
// 虽然我们使用的是插件来完成我们的功能，但是总体的处理逻辑是：

// 监听我们的输入文本
// 获取API的返回结果
// 对返回结果进行处理——如高亮输入文本、显示到页面上
// 处理用户点击事件
