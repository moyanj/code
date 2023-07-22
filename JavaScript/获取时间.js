
function getCurDate() {
    var d = new Date();
    // 年
    var years = d.getFullYear();
    // 月
    var month = add_zero(d.getMonth() + 1);
    // 日
    var days = add_zero(d.getDate());
    // 时
    var hours = add_zero(d.getHours());
    // 分
    var minutes = add_zero(d.getMinutes());
    // 秒
    var seconds = add_zero(d.getSeconds());
    // 拼接时分秒
    var ndate = hours + ":" + minutes + ":" + seconds;
    // 写入
    var divT = document.getElementById("h2");
    divT.innerHTML = ndate;
}
// 自动刷新
function add_zero(temp) {
    if (temp < 10) return "0" + temp;
    else return temp;
}
setInterval("getCurDate()", 100);
