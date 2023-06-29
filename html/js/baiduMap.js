
import { Button } from 'antd';
import 'antd/dist/antd.css';
import { DrawScene, MarkerDraw } from 'bmap-draw';
import { createRef, useEffect, useState } from 'react';

window.onload = function() {
    add_control()	
};

// // 监听鼠标滚轮事件
// window.addEventListener("wheel", function(event) {
// 	var delta = Math.sign(event.deltaY); // 获取滚轮滚动方向，1表示向下滚动，-1表示向上滚动

// 	// 根据滚动方向调用不同的函数
// 	if (delta > 0) {
// 		zoomIn();
// 	} else if (delta < 0) {
// 		zoomOut();
// 	}
// });


// 百度地图API功能
function G(id) {
    return document.getElementById(id);
}

var map = new BMap.Map("l-map");
map.centerAndZoom("北京",12);                   // 初始化地图,设置城市和地图级别。
map.enableScrollWheelZoom();
var top_left_control = new BMap.ScaleControl({anchor: BMAP_ANCHOR_TOP_LEFT});// 左上角，添加比例尺
var top_left_navigation = new BMap.NavigationControl();  //左上角，添加默认缩放平移控件
var top_right_navigation = new BMap.NavigationControl({anchor: BMAP_ANCHOR_TOP_RIGHT, type: BMAP_NAVIGATION_CONTROL_SMALL}); //右上角，仅包含平移和缩放按钮
/*缩放控件type有四种类型:
BMAP_NAVIGATION_CONTROL_SMALL：仅包含平移和缩放按钮；BMAP_NAVIGATION_CONTROL_PAN:仅包含平移按钮；BMAP_NAVIGATION_CONTROL_ZOOM：仅包含缩放按钮*/

//添加控件和比例尺
function add_control(){
    map.addControl(top_left_control);        
    map.addControl(top_left_navigation);     
    map.addControl(top_right_navigation);    
}

// 地图放大
function zoomIn() {
    map.zoomIn();
}

// 地图缩小
function zoomOut() {
    map.zoomOut();
}
var ac = new BMap.Autocomplete(    //建立一个自动完成的对象
    {"input" : "suggestId"
    ,"location" : map
});

ac.addEventListener("onhighlight", function(e) {  //鼠标放在下拉列表上的事件
var str = "";
    var _value = e.fromitem.value;
    var value = "";
    if (e.fromitem.index > -1) {
        value = _value.province +  _value.city +  _value.district +  _value.street +  _value.business;
    }    
    str = "FromItem<br />index = " + e.fromitem.index + "<br />value = " + value;
    
    value = "";
    if (e.toitem.index > -1) {
        _value = e.toitem.value;
        value = _value.province +  _value.city +  _value.district +  _value.street +  _value.business;
    }    
    str += "<br />ToItem<br />index = " + e.toitem.index + "<br />value = " + value;
    G("searchResultPanel").innerHTML = str;
});

var myValue;
ac.addEventListener("onconfirm", function(e) {    //鼠标点击下拉列表后的事件
var _value = e.item.value;
    myValue = _value.province +  _value.city +  _value.district +  _value.street +  _value.business;
    G("searchResultPanel").innerHTML ="onconfirm<br />index = " + e.item.index + "<br />myValue = " + myValue;
    
    setPlace();
});

function setPlace(){
    map.clearOverlays();    //清除地图上所有覆盖物
    function myFun(){
        var pp = local.getResults().getPoi(0).point;    //获取第一个智能搜索的结果
        map.centerAndZoom(pp, 18);
        map.addOverlay(new BMap.Marker(pp));    //添加标注
    }
    var local = new BMap.LocalSearch(map, { //智能搜索
        onSearchComplete: myFun
    });
    local.search(myValue);
}

// 尝试插入点: 1 创建标注；2 可以拖动标注；
var point = new BMap.Point(116.404, 39.915);
var marker = new BMap.Marker(point);  // 创建标注
map.addOverlay(marker);               // 将标注添加到地图中
marker.setAnimation(BMAP_ANIMATION_BOUNCE); //跳动的动画
marker.enableDragging();

// 尝试实现鼠标点击地图：返回该点的经纬度；
function showInfo(e){
    alert(e.point.lng + ", " + e.point.lat);
}
map.addEventListener("click", showInfo);

// 尝试设置起点和终点

var start_point = new BMap.Point(x1, y1);
var end_point = new BMap.Point(x2, y2);

var marker_start = new BMap.Marker(new BMap.Point(0, 0));  // 起点标注
var marker_end = new BMap.Marker(new BMap.Point(0, 0));    // 终点标注
map.addOverlay(marker_start);
map.addOverlay(marker_end);

// 获取起点和终点输入框
var startInput = document.getElementById("start_point");
var endInput = document.getElementById("end_point");

// 监听输入框内容变化事件
startInput.addEventListener("input", updateStartPoint);
endInput.addEventListener("input", updateEndPoint);

// 更新起点标注
function updateStartPoint() {
    var point = parsePoint(startInput.value);
    if (point) {
        marker_start.setPosition(point);
        map.panTo(point);
    }
}

// 更新终点标注
function updateEndPoint() {
    var point = parsePoint(endInput.value);
    if (point) {
        marker_end.setPosition(point);
        map.panTo(point);
    }
}

// 解析经纬度字符串为点坐标
function parsePoint(str) {
    var parts = str.split(",");
    if (parts.length === 2) {
        var lng = parseFloat(parts[0]);
        var lat = parseFloat(parts[1]);
        if (!isNaN(lng) && !isNaN(lat)) {
            return new BMap.Point(lng, lat);
        }
    }
    return null;
}
