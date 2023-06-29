window.onload = function() {
    add_control()	
};   

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

// 尝试实现鼠标点击地图：返回该点的经纬度；
function showInfo(e){
    var lng = e.point.lng;
    var lat = e.point.lat;
    alert(e.point.lng + ", " + e.point.lat);
}
map.addEventListener("click", showInfo);

// 尝试设置起点和终点

var marker_start = new BMap.Marker(new BMap.Point(0, 0));  // 起点标注
var marker_end = new BMap.Marker(new BMap.Point(0, 0));    // 终点标注
map.addOverlay(marker_start);
map.addOverlay(marker_end);
marker_start.setAnimation(BMAP_ANIMATION_BOUNCE); //跳动的动画	
marker_end.setAnimation(BMAP_ANIMATION_BOUNCE); //跳动的动画
marker_start.enableDragging();
marker_end.enableDragging();

start_point = new BMap.Point(0, 0);
end_point = new BMap.Point(0, 0);
// 提交按钮点击事件
var submitBtn = document.getElementById("submitBtn");
submitBtn.addEventListener("click", function() {
    // 获取输入框的值
    var startPointInput = document.getElementById("start_point").value;
    var endPointInput = document.getElementById("end_point").value;
    // 拆分经纬度字符串
    var startPointArr = startPointInput.split(",");
    var endPointArr = endPointInput.split(",");
    // 更新起点和终点的经纬度
    var x1 = startPointArr[0];
    var y1 = startPointArr[1];
    var x2 = endPointArr[0];
    var y2 = endPointArr[1];
    // 更新起点和终点的标注位置
    start_point = new BMap.Point(x1, y1);
    end_point = new BMap.Point(x2, y2);
    marker_start.setPosition(start_point);
    marker_end.setPosition(end_point);
});		

var routePolicy = [BMAP_TRANSIT_POLICY_RECOMMEND,BMAP_TRANSIT_POLICY_LEAST_TIME,BMAP_TRANSIT_POLICY_LEAST_TRANSFER,BMAP_TRANSIT_POLICY_LEAST_WALKING,BMAP_TRANSIT_POLICY_AVOID_SUBWAYS,BMAP_TRANSIT_POLICY_FIRST_SUBWAYS];
var transit = new BMap.TransitRoute(map, {
        renderOptions: {
            map: map, 
            autoViewport: true,
            panel: 'result'
        },
        policy: 0,
});

// 搜索按钮点击事件
var searchBtn = document.getElementById("searchBtn");
searchBtn.addEventListener("click", function() {
    map.clearOverlays();
    var i= $("#driving_way select").val();
    search(start_point,end_point,routePolicy[i]); 
    function search(start_point,end_point,route){ 
        transit.setPolicy(route);
        transit.search(start_point,end_point);
    }
});

// Car 搜索按钮点击事件
var searchBtn = document.getElementById("carBtn");
searchBtn.addEventListener("click", function() {
    map.clearOverlays();
    var driving = new BMap.DrivingRoute(map, {
        renderOptions:{
            map: map, autoViewport: true
        }
    });
    driving.search(start_point,end_point);	
});

// Bike 搜索按钮点击事件
$("#bikeBtn").click(function()  {
    map.clearOverlays();
    var riding = new BMap.RidingRoute(map, { 
        renderOptions: { 
            map: map, 
            autoViewport: true 
        }
    });
    riding.search(start_point,end_point);	
});

// Foot 搜索按钮点击事件
$("#footBtn").click(function()  {
    map.clearOverlays();
    var walking = new BMap.WalkingRoute(map, { 
        renderOptions: { 
            map: map, 
            autoViewport: true 
        }
    });
    walking.search(start_point,end_point);	
});



