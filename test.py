!function(n){if(!1===n)return!1;
if("function"==typeof window.onerror)return!1;
    var t=function(n,t){var e=null;for(e in t)e in n||(n[e]=t[e]);return n},e=function(n){var t=null,e="";for(t in n)e+='"'+t+'":"'+n[t]+'",';return e="{"+e.slice(0,-1)+"}"},a=function(){var n=function(n){return"function"==typeof n},t=function(){return Array.prototype.slice.call(arguments[0],0)},e=function(){if(!(this instanceof a))return new a;this._functions={},this._id=0,this._nextId=0,this._arg=[]};return e.prototype={_middleFun:function(e,a){var i=this._functions;return function(){var o=i[a];n(o)||(o=function(){}),e.apply(o,t(arguments))}},_wrap:function(n){var t=this._id,e=this._id+=1;this._functions[t]=this._middleFun(n,e)},get:function(t){return!!n(t)&&(this._wrap(t),this)},setArg:function(){this._arg=t(arguments)},run:function(){var n=this._arg;return this._functions[0].apply(null,n),this}},e}(),i=function(n,t){document.documentMode<=8?n.onreadystatechange=function(e){"loaded"===n.readyState&&t(e)}:n.onload=t},o=function(n,t,e){i(n,function(){var a,i,o=n.status;if(-1!==["text","json"].indexOf(e)){if(i=a=n.responseText,"json"===e)try{i=JSON.parse(a)}catch(n){i=a}}else i=n.response;i={status:o,message:i},t("success",i)}),n.onerror=function(n){t("error",n)},n.ontimeout=function(n){t("timeout",n)}},s=(function(){var n=function(n){var t=n.url,e=n.timeout,a=n.data,i=n.dataType;i=i||"text";var s=new XMLHttpRequest,r=this;"number"==typeof e&&(s.timeout=e),"responseType"in s&&(s.responseType="json"===i?"text":i),o(s,r,i),s.open("get",a?t+"?"+a:t,!0),s.send(null)}}(),function(){var n=function(n){var t=n.url,e=n.timeout,a=n.data,i=n.dataType;i=i||"text";var s=new XMLHttpRequest,r=this;"number"==typeof e&&(s.timeout=e),"responseType"in s&&(s.responseType="json"===i?"text":i),o(s,r,i),s.open("post",t,!0),s.setRequestHeader("Content-type","application/x-www-form-urlencoded"),s.send(a)};return function(t){var e=new a;return e.setArg(t),e.get(n),e}}()),r=(function(){var n=document.createElement("div");document.addEventListener}(),{version:"0.1",list:["request","origin","status","error","href"],init:function(n){for(var t=0,e=n.length,a=null,i=this.list,o={};t<e;t+=1)a=n[t],-1!==i.indexOf(a)&&(o[a]=this[a]);return o},href:location.href,request:{url:"/monitor/endFront/jsWarn.json",dataType:"json",method:"post"},origin:{topic:"root.monitor.yundunconsole.jswarn"},status:{0:"no crossDomain",1:""}}),c=function(){return{_bindAttr:function(n){for(var t=["info","src","lineno","colno","error","href"],e=0,a=t.length,i=null,o="";e<a;e+=1)i=t[e],o+=i+": "+n[e]+",";return encodeURI(o.slice(0,-1))},mark:function(){return[]}(),check:function(n,t,e){var a=null,i=this.mark,o=null;return n[1]?(o=n[1]+n[2]+n[3],-1===i.indexOf(o)?(i.push(o),a=this._bindAttr(n)):a=!1):a=!1,a},pack:function(n,a){return n=t({content:n},a),n="message="+e(n)}}},l=function(n,t){if(n=n||r,t=t||c(),!(this instanceof l))return new l(n,t);this.config=n.init(n.list),this.filter=t};l.prototype={setUrl:function(n){return this.url=n,this},export:function(){var n=this.config,t=this.filter,e=n.request,a=this.url;a=a||e.url;var i=n.href;return function(o,r,c,l,d){var u=t.check([o,r,c,l,d,i],n.status,i);if(!1===u)return!1;u=t.pack(u,n.origin),s({url:a,dataType:e.dataType,data:u}).get(function(n,t){}).run()}}};var d=l();window.onerror=d.export(),"function"==typeof define&&define.amd?define("errorControl",[],function(){return l}):window.errorControl=l}(null===window.onerror&&window),function(){if(window.angular&&window.jQuery&&window.$){var n=(this.pageCommon||{}).yundunProducts,t=n&&angular.fromJson(n),e=t||[{id:"all",nav:!1,name:"\u4e91\u76fe\uff08\u5168\u90e8\u4ea7\u54c1\uff09"},{id:"sas",name:"\u6001\u52bf\u611f\u77e5"},{id:"aqs",intl:!0,name:"\u670d\u52a1\u5668\u5b89\u5168(\u5b89\u9a91\u58eb)",en:"Server Guard"},{id:"ddos",intl:!0,jp:!0,name:"DDoS\u9632\u62a4",newStyle:!0,en:"Anti-DDoS Service"},{id:"waf",intl:!0,name:"Web\u5e94\u7528\u9632\u706b\u5899",newStyle:!0,en:"Web Application Firewall"},{id:"xz",name:"\u5148\u77e5(\u5b89\u5168\u60c5\u62a5)"},{id:"mss",name:"\u5b89\u5168\u7ba1\u5bb6"},{id:"hsm",intl:!1,name:"\u52a0\u5bc6\u670d\u52a1"},{id:"cts",name:"\u7eff\u7f51",en:"Content Security"},{id:"afs",name:"\u6570\u636e\u98ce\u63a7\u670d\u52a1",en:"Antifraud Service"},{id:"jaq",intl:!0,name:"\u79fb\u52a8\u5b89\u5168",en:"Mobile Security"},{id:"cas",intl:!0,name:"\u8bc1\u4e66\u670d\u52a1",en:"SSL Certificates Service"},{id:"slm",nav:!1,name:"\u5b89\u5168\u65e5\u5fd7\u7ba1\u7406"},{id:"sppc",name:"\u5b89\u5168\u5408\u4f5c\u4f19\u4f34\u4ea7\u54c1"},{id:"refund",nav:!1,name:"5\u5929\u65e0\u7406\u7531\u9000\u6b3e"},{id:"safe",nav:!1,intl:!0,name:"\u5b89\u5168\u589e\u5f3aECS"},{id:"sc",nav:!1,intl:!0,jp:!0,name:"\u5b89\u5168\u7ba1\u63a7\u5e73\u53f0",en:"Security control"},{id:"cfw",name:"\u4e91\u9632\u706b\u5899"},{id:"dbaudit",name:"\u6570\u636e\u5e93\u5ba1\u8ba1"},{id:"bastion",name:"\u4e91\u5821\u5792\u673a"},{id:"avds",name:"\u6f0f\u6d1e\u626b\u63cf"}];this.ydProducts2016=e;var a=this;!function(n){var t={},e=(a.CURRENT_SITE||"CN").toLocaleLowerCase(),i=!("ZH"==(a.CURRENT_LOCALE||"").toLocaleUpperCase()),o=i?"Alicloud Security":"\u4e91\u76fe",s=i?"":"\u7ba1\u7406\u63a7\u5236\u53f0",r=["ddos","cas"];$(function(){$("body").addClass("yundun-console-"+(i?"en":"zh")+"-lang-wrap")}),function(){"cn"!=e?(!function(){"ALL"==a.P.toLocaleUpperCase()&&location.replace((location.pathname||"/")+"?p=ddos")}(),angular.forEach(n,function(n){var a=n.id;!0!==n[e]&&"all"!==a||(t[a]=n)})):angular.forEach(n,function(n){t[n.id]=n})}();var c={},l={sas:[/^\/slm\/settings\/setSpace$/],cts:[/^\/greenWeb/],ddos:[/^\/detail\/detectddos/,/^\/detail\/waf/,/^\/buyService/,/^\/cloudsLayer/],aqs:[/^\/sas\/host\/software$/],mss:[/^\/insurance/,/^\/sos/]};c.init=function(){this.getProduct(),this.regionRedirect(this.product),this.product||(this.getInfo(),this.check())},c.getProduct=function(){var n="all",t=location.href.match(/[\?&]p=([a-z]{2,9})/);return t&&(n=t[1]),this.product=n,n},c.getInfo=function(){var n=window.location;return this.href=(n.href||"").replace(/#\/\S+/,""),this.hash=(n.hash||"").replace(/^#/,""),this},c.check=function(){var n=(this.hash,this.scanRule());n?this.redirect(n):this.redirect(this.getMatchProduct())},c.scanRule=function(){var n,t=this.hash;for(var e in l){n=l[e];for(var a=0,i=n.length;a<i;a++)if(n[a].test(t))return e}},c.getMatchProduct=function(){var n=this.hash,t=n.match(/^\/([a-z]{2,9})/);if(t)return t[1]},c.redirect=function(n){var t;n&&"/sas/overviews"!==this.hash&&(t=this.href,window.location.replace([t,(-1!=t.indexOf("?")?"&":"?")+"p=",n,"#",this.hash].join("")))},c.regionRedirect=function(n){if(void 0!==n&&!(r.indexOf(n)>-1))for(var t=(location.href||"").replace(/#\/\S+/,""),e=["yundun-ap-northeast-1.console.aliyun","yundun-eu-central-1.console.aliyun","yundun-ap-southeast-2.console.aliyun","yundun-me-east-1.console.aliyun"],a=0,i=e.length;a<i;a++)t.indexOf(e[a])>-1&&window.location.replace(t.replace(/yundun(\S*).console.aliyun/g,"yundun.console.aliyun"))},function(){var n=a.P,e=t[n],r=window.location,c=[r.protocol,"//",r.host,r.pathname].join("");if(e){if("localhost"!=r.hostname){var l=i?e.en||e.name||"":e.name||"";"all"==n&&(l=""),document.title=(i?"":o)+l+s}return!0}return window.location.href=c,!1}()&&c.init()}(e),function(n){var t={};t.run=function(){$(document).on("click",function(){t.init()}),window.setTimeout(function(){t.init()},500)},t.init=function(){$("#ydmenu2016").size()>0||(this.container=$(".topbar-nav-list"),this.render())},t.render=function(){this.container.html('<div id="ydmenu2016" class="topbar-nav-item"><ul>'+this.getMenu()+"</ul></div>")},t.getMenu=function(){var t,e,a,i=[];n[0].nav=!0;for(var o=0,s=n.length;o<s;o++)e=n[o],!1!==e.nav&&(a=e.id,t='<li><a href="?p='+a+'">',t+='<span class="topbar-nav-item-icon icon-'+a+' icon-logo1"></span>',t+="<span>"+e.name+"</span></a></li>",i.push(t));return i.join("")},/aliyun\.com$/.test(window.location.hostname)||t.run()}(angular.copy(e)),function(){if(window.JSON&&"CN"==a.CURRENT_SITE){({init:function(){this.currentProduct=a.P,this.getConfig(),this.config.clearCache&&this.clearCache(),this.isEnabled()&&this.render()},getConfig:function(){var n=this.parseConfig();this.config=n,this.text=n.title,this.url=n.url,this.enabled=n.enabled,this.style=n.style,this.position=n.position,this.getProductConfig()},isEnabled:function(){return!this.noNotice(!0)&&this.enabled},parseConfig:function(){var n=JSON.parse((a.pageCommon||{}).yundunNotice||"{}");return n=n.id?n:{id:"2016110301",title:"\u963f\u91cc\u4e91\u5b98\u7f51",url:"https://www.aliyun.com",enabled:!1,clearCache:!1,products:{all:{url:"https://yundun.aliyun.com",title:"\u4e91\u76fe\u5b98\u7f51",enabled:!0},waf:{url:"https://www.aliyun.com/product/waf",title:"WAF\u4ea7\u54c1\u5b98\u7f51",enabled:!0,style:2},sas:{url:"https://www.aliyun.com/product/sas",title:"SAS\u4ea7\u54c1\u5b98\u7f51",enabled:!0,position:"absolute"},aqs:{enabled:!1}},style:3,linkStyle:1}},getProductConfig:function(){var n=(this.config.products||{})[this.currentProduct];n&&(this.text=n.title||this.text,this.url=n.url||this.url,this.enabled=!!n.enabled,this.style=n.style,this.position=n.position)},create:function(){var n=this,t=(this.config,"position: "+(this.position||"relative")+"; z-index: 99999; width: 100%; color: #24B1FF;"),e={1:"warning",2:"success",3:"danger"}[this.style||1],a=$('<a href="javascript:;" style="position: absolute; right: 15px;">\u5173\u95ed</a>'),i=$(['<div style="'+t+'" class="alert alert-'+e+'">','<a href="'+this.url+'" target="_blank">'+this.text+"</a>","</div>"].join(""));return i.append(a),a.on("click",function(){i.remove(),n.noNotice()}),i},render:function(){var n=this,t=$(".viewFramework-product-body");if(0==t.size())return void window.setTimeout(function(){n.render()},50);t.prepend(this.create())},noNotice:function(n){var t=this.config.id||"2016110301",e=window.localStorage;if(e&&"CN"==a.CURRENT_SITE){var i="__yd_ad_"+[this.currentProduct,t].join("_"),o=!!e.getItem(i);if(n)return o;e.setItem(i,(new Date).getTime())}},clearCache:function(){for(var n in localStorage)/^__yd_ad_(\w|_)+/g.test(n)&&localStorage.removeItem(n)}}).init()}}()}}.call(window.ALIYUN_YUNDUN_CONSOLE_CONFIG||{}),function(n){var t,e=[],a=[5,10,15],i="166, 180, 190",o={Ajax:function(n,t,e,a){var i={__preventCache:(new Date).getTime()};i=$.extend(i,e||{}),$.ajax({url:"/"+n,type:"get",dataType:"json",data:i,timeout:5e3,success:function(n){var e=n.data||{};t&&t(e)},error:function(n){a&&a(n)}})},getWaveColor:function(n,t){return"rgba("+n+","+t+")"},formatDate:function(n,t,e){var a,i=(new Date).getTime(),o=n-i;if(o<1296e6){var s=Math.floor(o/864e5),r="5176.2020520110.com."+e;a=s<1?'<span class="text-warning">\u4e0d\u8db31\u5929\u540e\u5230\u671f </span>':'<span class="text-warning">'+s+"\u5929\u540e\u5230\u671f </span>",t&&(a+='<a class="margin-left" href="'+t+'" target="_blank" data-spm-anchor-id="'+r+'">\u7eed\u8d39</a>')}return a}},s={getSasInfo:function(){var n=window.ALIYUN_YUNDUN_CONSOLE_CONFIG,t=new Date(n.SAS_SALES_OVERDUE_TIME).getTime();if(!n.IS_SAS_OPENING)return $(".sas-p").hide(),e.push(0),e.push(0),void e.push(0);o.Ajax("sas/overviews/getEventsCount.json",function(n){var a=[];e.push(n.event||0),n.event&&a.push('<span>\u7d27\u6025\u4e8b\u4ef6<a data-spm-anchor-id="5176.2020520110.com.2" class="text-warning" href="/?p=sas#/sas/securityEvent/list">'+n.event+"\u4e2a</a></span>"),e.push(n.vul||0),n.vul&&a.push('<span>\u6f0f\u6d1e<a data-spm-anchor-id="5176.2020520110.com.3" class="text-warning" href="/?p=sas#/sas/apps/vul">'+n.vul+"\u4e2a</a></span>"),e.push(n.threat||0),n.threat&&a.push('<span>\u653b\u51fb\u6b21\u6570<a data-spm-anchor-id="5176.2020520110.com.4" class="text-warning" href="/?p=sas#/sas/apps/attack">'+n.threat+"\u6b21</a></span>");var i=o.formatDate(t,"/buy?id=sas#/renew",5);i&&a.push(i),0==a.length?$(".sas-p").hide():$(".sas-p .p-main").html(a.join(""))})},getAqsInfo:function(){o.Ajax("aqs/buy/getSummary.json",function(n){var t=n.buyType;if(!n.buyStatus)return $(".aqs-p").hide(),e.push(0),e.push(0),void e.push(0);o.Ajax("aqs/init/getStatistics.json",function(a){var i=[];e.push(a.health||0),a.health&&i.push('<span>\u9ad8\u5371\u57fa\u7ebf<a data-spm-anchor-id="5176.2020520110.com.6" class="text-warning" href="/?p=aqs#/aqs/models/safeCheck">'+a.health+"\u53f0</a></span>"),e.push(a.trojan||0),a.trojan&&i.push('<span>\u53d1\u73b0\u6728\u9a6c<a data-spm-anchor-id="5176.2020520110.com.7" class="text-warning" href="/?p=aqs#/aqs/models/killTrojan">'+a.trojan+"\u4e2a</a></span>"),e.push(a.patch||0),a.patch&&i.push('<span>\u6f0f\u6d1e\u5f85\u4fee\u590d<a data-spm-anchor-id="5176.2020520110.com.8" class="text-warning" href="/?p=aqs#/aqs/models/patchManage">'+a.patch+"\u4e2a</a></span>");var s="safePoint"==t?"//common-buy.aliyun.com/?commodityCode=vipaegisbag#/":"",r=o.formatDate(n.expireDate,s,9);r&&i.push(r),0==i.length?$(".aqs-p").hide():$(".aqs-p .p-main").html(i.join(""))})})},getWafInfo:function(){o.Ajax("waf/report/waf/webAttackCount.json",function(n){var t=[];e.push(n.attackCount||0),n.attackCount&&t.push('<span>\u653b\u51fb\u6b21\u6570<a data-spm-anchor-id="5176.2020520110.com.10" class="text-warning" href="/?p=waf#/waf/main/report/web">'+n.attackCount+"\u6b21</a></span>"),o.Ajax("waf/package/info.json?region=cn",function(n){var e="//common-buy.aliyun.com/?commodityCode=waf&orderType=RENEW&instanceId="+n.instanceId+"#/renew",a=o.formatDate(n.expireTime,e,11);a&&t.push(a),0==t.length?$(".waf-p").hide():$(".waf-p .p-main").html(t.join(""))})},{domains:'[""]',time:"day",region:"cn"})},getDdosInfo:function(){o.Ajax("highdefend/details/getInstanceList.json?region=cn",function(n){var t={};n.list&&0!=n.list.length&&(t=n.list[0]);var e=t.orderNum,a=o.formatDate(t.expireTime,"javascript:;");o.Ajax("highdefend/details/ddosOrderStatic.json?orderNum="+e,function(n){var t=[];n.peakFlow&&(total_num+=n.peakFlow,t.push('<span>\u653b\u51fb\u5cf0\u503c<a data-spm-anchor-id="5176.2020520110.com.12" class="text-warning" href="javascript:;">'+n.peakFlow+"Gb</a></span>")),a&&t.push(a),0==t.length?$(".ddos-p").hide():$(".ddos-p .p-main").html(t.join(""))})})},getXzInfo:function(){o.Ajax("xianzhi/v2/company/isHasRewardOrMass.json",function(n){if(n.mass&&n.mass.status){var t=n.mass.purchaseProductId;o.Ajax("xianzhi/v2/company/massRewardOverview.json",function(n){var t=[],a=n.mass||{};e.push(a.unFixedFlawCount||0),a.unFixedFlawCount&&t.push('<span>\u5f85\u4fee\u590d\u6f0f\u6d1e<a data-spm-anchor-id="5176.2020520110.com.13" class="text-warning" href="/?p=xz#/overviews">'+a.unFixedFlawCount+"\u4e2a</a></span>"),a.currentMoney<=0&&t.push('<span class="text-warning">\u5df2\u6b20\u8d39 <a data-spm-anchor-id="5176.2020520110.com.14" class="margin-left" href="/buy?id=xianzhi#/prepay">\u5145\u503c</span>'),0==t.length?$(".xz-p").hide():$(".xz-p .p-main").html(t.join(""))},{purchaseProductId:t})}else e.push(0),$(".xz-p").hide()})},getMssInfo:function(){o.Ajax("mssp/task/getSummary.json",function(n){var t=[];e.push(n.taskInProcess||0),n.taskInProcess&&t.push('<span>\u5f85\u5904\u7406\u4efb\u52a1<a data-spm-anchor-id="5176.2020520110.com.15" class="text-warning" href="/?p=mss#/mss/task">'+n.taskInProcess+"\u4e2a</a></span>"),0==t.length?$(".mss-p").hide():$(".mss-p .p-main").html(t.join(""))})},getGreenInfo:function(){o.Ajax("greenweb/main/homepageDashboard.json",function(n){var t=[];e.push(n.currentRiskNum||0),n.currentRiskNum&&t.push('<span>\u7591\u4f3c\u8fdd\u89c4URl<a data-spm-anchor-id="5176.2020520110.com.16" class="text-warning" href="/?p=cts#/greenWeb/contentCheck?inviteCode=cs">'+n.currentRiskNum+"\u4e2a</a></span>"),0==t.length?$(".green-p").hide():$(".green-p .p-main").html(t.join(""))})},getAfsInfo:function(){o.Ajax("riskassessment/riskAssessmentTodayCount/todayCount.json",function(n){var t=[];e.push(n.total||0),n.total&&t.push('<span>\u8bc6\u522b\u98ce\u9669\u4e8b\u4ef6<a data-spm-anchor-id="5176.2020520110.com.17" class="text-warning" href="/?p=afs#/afs/antifraud">'+n.total+"\u4e2a</a></span>"),0==t.length?$(".afs-p").hide():$(".afs-p .p-main").html(t.join(""))})},getInfoLists:function(){o.Ajax("yundun/activity/queryActivity.json",function(n){var t=n.securityUpdate&&n.securityUpdate.lists||[],e=[];$.each(t,function(n,t){var a="5176.2020520110.com.100"+n,i='<li><a target="_blank" data-spm-anchor-id="'+a+'" href="'+t.link+'"><span class="time">'+t.date+"</span>"+t.title+"</a></li>";e.push(i)}),$(".info-lists").html(e.join(""))})},initRiskNum:function(){var n=$(".product-info-layer .one-p"),t=0;n.each(function(n,e){"none"!=e.style.display&&(t+=1)});var e=t>9?"9+":t;$(".btn-show-layer span.num").html(e)},drawWave:function(){t=window.requestAnimationFrame&&requestAnimationFrame(s.drawWave);var n=document.getElementById("wave-can"),e=n.getContext("2d");e.clearRect(0,0,60,30),e.lineWidth=1.5;for(var r=0;r<a.length;r++){a[r]>22&&(a[r]=5),a[r]+=.08;var c=1-a[r]/22;e.strokeStyle=o.getWaveColor(i,c),e.beginPath(),e.arc(26,15,a[r],.8*Math.PI,-.8*Math.PI),e.stroke(),e.beginPath(),e.arc(34,15,a[r],-.2*Math.PI,.2*Math.PI),e.stroke()}},bindEvent:function(){var n=function(){i="166, 180, 90",$(".btn-show-layer").removeClass("text-danger"),$(".btn-show-layer .notice").removeClass("notice-shake"),$(".product-info-layer").fadeIn(function(){$(".modal-content").slideDown(),window.cancelAnimationFrame&&cancelAnimationFrame(t)})},e=function(){$(".modal-content").slideUp(function(){$(".product-info-layer").fadeOut()})};$(".btn-hide").on("click",function(){e()}),$(".btn-show-layer").on("click",function(){n(),sessionStorage.comTopBtnClicked=!0}),$(".product-info-layer").on("click",function(){e()}),$(".product-info-layer .modal-content").on("click",function(n){n.stopPropagation()})}},r=function(n){var t=["<style>",".btn-show-layer {display:block;min-width: 60px;height: 30px;position: fixed;z-index: 10000;top: 50px;left: 50%;background: #fff;line-height: 30px;box-shadow: 0 3px 8px #D8D8D8;border-bottom-left-radius: 6px;border-bottom-right-radius: 6px;margin-left: -40px;color: #90A0AE;}",".btn-show-layer .notice {position: absolute;left: 24px;top: 9px;}",".btn-show-layer .notice-shake {animation: bellShake 1.5s ease infinite;-webkit-animation: bellShake 1.5s ease infinite;}",".btn-show-layer .num {display: inline-block;font-size: 18px;padding-right:10px;}",".btn-show-layer canvas {display: inline-block;float: left;}",".btn-show-layer:hover {cursor: pointer;background: #f5f5f5;color: #90A0AE;}",".product-info-layer {z-index: 100001;margin-top: -1px;background: rgba(255,255,255,.5);font-family: PingFangSC-Regular;position: fixed;top: 0;}",".product-info-layer .modal-dialog {margin-top: 50px !important;}",".product-info-layer .modal-header {padding: 6px 15px;background: #F4F8FB;color: #576369;}",".product-info-layer .modal-title {font-family: PingFangSC-Regular;}",".product-info-layer .modal-title .icon-yundun {margin-right: 4px;font-size: 15px;position: relative;bottom: -1px;}",".product-info-layer .btn-hide-layer {width: 200px;height: 10px;background: red;}",".product-info-layer .one-p {height: 35px;line-height: 35px;border-bottom: 1px dashed #C4D6DF;padding-top: 1px;}",".product-info-layer .p-name {color: #576369;font-weight: bold;padding: 0px;text-align: right;width: 100px;}",".product-info-layer .one-p .p-main {padding-left: 5px;width: 450px;}",".product-info-layer .one-p .p-main span {margin-right: 20px;color: #666;}",".product-info-layer .one-p .p-main a {margin-left: 4px;color: rgb(0,198,255);}",".product-info-layer .info-lists {min-height: 10px;overflow: hidden;margin-bottom: 20px;}",".product-info-layer .info-lists li {list-style: none;height: 24px;line-height: 24px;width: 50%;float: left;color: #666;}",".product-info-layer .info-lists li a {color: #333;}",".product-info-layer .info-lists li a:hover, .product-info-layer .info-lists li a:focus {text-decoration: none;}",".product-info-layer .info-lists li a:hover, .product-info-layer .info-lists li a:hover .time {color: #06c;}",".product-info-layer .info-lists li .time {color: #90A0AE;margin-right: 8px;position: relative;bottom: -1px;}",".product-info-layer .btn-hide {display:block; width: 80px;margin: 0 auto;color: #fff;text-align: center;height: 15px;line-height: 16px;background: rgb(255,108,97);border-radius: 6px;border-bottom-left-radius: 0;border-bottom-right-radius: 0;}",".product-info-layer .btn-hide:hover {opacity: 0.8;cursor:pointer;text-decoration:none;}","@keyframes bellShake {from {transform: scale3d(1, 1, 1);}10%, 20% {transform: scale3d(.9, .9, .9) rotate3d(0, 0, 1, -3deg);}30%, 50%, 70%, 90% {transform: scale3d(1.1, 1.1, 1.1) rotate3d(0, 0, 1, 3deg);}40%, 60%, 80% {transform: scale3d(1.1, 1.1, 1.1) rotate3d(0, 0, 1, -3deg);}to {transform: scale3d(1, 1, 1);}}","</style>"];n.prepend(t.join(""))},c=function(n,t){n.prepend(t);var e=['<div class="product-info-layer modal" style="display: none;">','<div class="modal-dialog"><div class="modal-content" style="display: none;">','<div class="modal-header">','<h5 class="modal-title"><span class="icon-yundun text-primary"></span>\u4e91\u76fe\u603b\u89c8\u4fe1\u606f<span class="text-size-12">\uff08\u4eca\u65e5\u6570\u636e\uff09</span></h5></div>','<div class="modal-body clearfix">','<div class="one-p sas-p"><div class="col-sm-2 p-name">\u6001\u52bf\u611f\u77e5\uff1a</div><div class="col-sm-10 p-main"></div></div>','<div class="one-p aqs-p"><div class="col-sm-2 p-name">\u670d\u52a1\u5668\u5b89\u5168\uff1a</div><div class="col-sm-10 p-main"></div></div>','<div class="one-p waf-p"><div class="col-sm-2 p-name">Web\u5e94\u7528\u9632\u706b\u5899\uff1a</div><div class="col-sm-10 p-main"></div></div>','<div class="one-p xz-p"><div class="col-sm-2 p-name">\u5148\u77e5\uff1a</div><div class="col-sm-10 p-main"></div></div>','<div class="one-p mss-p"><div class="col-sm-2 p-name">\u5b89\u5168\u7ba1\u5bb6\uff1a</div><div class="col-sm-10 p-main"></div></div>','<div class="one-p green-p"><div class="col-sm-2 p-name">\u7eff\u7f51\uff1a</div><div class="col-sm-10 p-main"></div></div>','<div class="one-p afs-p"><div class="col-sm-2 p-name">\u6570\u636e\u98ce\u63a7\uff1a</div><div class="col-sm-10 p-main"></div></div>',"</div>",'<ul class="info-lists"></ul>','<a href="javascript:;" class="btn-hide" data-spm-anchor-id="5176.2020520110.com.18">\u25b2</a>',"</div></div></div>"];t.html(e.join(""))};if(n.ydOverview)return void console.error("ydOverview already exsis.");n.ydOverview={venderProductInfo:function(){var n=setInterval(function(){var a=$(".viewFramework-product-body"),o=$('<div id="yd-product-info-layer" data-spm="com"></div>');if(0!=a.size()){clearInterval(n),r(a),c(a,o),s.getSasInfo(),s.getAqsInfo(),s.getWafInfo(),s.getXzInfo(),s.getMssInfo(),s.getGreenInfo(),s.getAfsInfo(),s.getInfoLists();var l=setInterval(function(){if(e.length>=11){clearInterval(l);var n=0;e.map(function(t){n+=t});var a='<a href="javascript:;" class="btn-show-layer" data-spm-anchor-id="5176.2020520110.com.1"><i class="notice glyphicon glyphicon-bell"></i><canvas id="wave-can" width="60" height="30"></canvas></a>';if(n>0){var r="",c="";sessionStorage.comTopBtnClicked||(i="255, 0, 0",r="text-danger",c="notice-shake"),a='<a href="javascript:;" data-spm-anchor-id="5176.2020520110.com.1" class="btn-show-layer '+r+'"><i class="notice '+c+' glyphicon glyphicon-bell"></i><canvas id="wave-can" width="60" height="30"></canvas><span class="num"></span></a>'}o.prepend(a),s.drawWave(),s.bindEvent(),sessionStorage.comTopBtnClicked&&window.cancelAnimationFrame&&cancelAnimationFrame(t),setTimeout(function(){s.initRiskNum()},10)}},30)}},30)}}}(window),function(){var n=!1,t=window.ALIYUN_YUNDUN_CONSOLE_CONFIG||{},e=t.pageCommon||{},a=(window.location.href||"").replace(/#\/\S+/,""),i="true"==e.yundunFloatLayerHide,o="true"==e.yundunFeedBackHide;if(window.JSON){var s=JSON.parse(e.yundunWhiteDomainList||"[]"),r=JSON.parse(e.yundunBlackProductList||"[]"),c={getURLParam:function(n){return decodeURIComponent((new RegExp("[?|&]"+n+"=([^&;]+?)(&|#|;|$)","ig").exec(location.hash)||[,""])[1].replace(/\+/g,"%20"))||null},setHideFlag:function(){"CN"!==t.CURRENT_SITE&&(n=!0),i&&(n=!0),window.isVirtualMachine&&(n=!0),(c.getURLParam("isEcs")||c.getURLParam("hideLayer"))&&(n=!0),r.map(function(e){t.P==e&&(n=!0)})}},l={hideFeedBack:function(){var n=setInterval(function(){var t=$(".feedback-container");0!=t.size()&&(clearInterval(n),t.hide())},50)}};ydOverview.init=function(){if(o&&l.hideFeedBack(),c.setHideFlag(),!n)for(var t=0,e=s.length;t<e;t++)if(a.indexOf(s[t])>-1){ydOverview.venderProductInfo();break}},ydOverview.init()}}();