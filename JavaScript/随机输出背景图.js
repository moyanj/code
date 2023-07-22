
// 定义壁纸路径
var bodyBgs = [];
bodyBgs[0] = "https://img1.imgtp.com/2022/07/20/FaDiFBf1.png";
bodyBgs[1] = "https://img1.imgtp.com/2022/07/20/mNuE9fDE.png";
bodyBgs[2] = "https://img1.imgtp.com/2022/07/20/fQ17p7hD.png";
bodyBgs[3] = "https://img1.imgtp.com/2022/07/20/16Ubw8al.png";
bodyBgs[4] = "https://img1.imgtp.com/2022/07/20/fOWchfrv.png";
bodyBgs[5] = "https://img1.imgtp.com/2022/07/20/xNQfHie4.png";
bodyBgs[6] = "https://img1.imgtp.com/2022/07/20/79C8mvww.png";
bodyBgs[7] = "https://img1.imgtp.com/2022/07/20/JbyoBABi.png";
bodyBgs[8] = "https://img1.imgtp.com/2022/07/20/fQ17p7hD.png";
bodyBgs[9] = "https://img1.imgtp.com/2022/07/20/WJGmseWA.png";
bodyBgs[10] = "https://img1.imgtp.com/2022/07/20/N1iPi8NQ.png";
bodyBgs[11] = "https://img1.imgtp.com/2022/07/20/tjBVdsPd.png";
bodyBgs[12] = "https://img1.imgtp.com/2022/07/20/fkQMWuiV.png";
bodyBgs[13] = "https://img1.imgtp.com/2022/07/20/FaDiFBf1.png";
bodyBgs[14] = "https://img1.imgtp.com/2022/07/20/rutgs0f2.png";
bodyBgs[15] = "https://img1.imgtp.com/2022/07/20/3oA0WvlT.png";
// 生成随机数
var randomBgIndex = Math.round(Math.random() * 15);
//输出随机的背景图
document.write('<style>body{background:url(' + bodyBgs[randomBgIndex] + ') no-repeat;background-size:cover;}</style>');
// console.log(randomBgIndex);
// console.log(bodyBgs[randomBgIndex])