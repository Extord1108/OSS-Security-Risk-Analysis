module.exports={
  publicPath:'./',
  outputDir: (process.env.NODE_ENV === "production") ? 'smart' : 'test', // 不同的环境打不同包名
  devServer:{
         // hot:true,//是否自动保存
        open : true,//是否自动启动
        port : 8080,//默认端口号
        // host : "0.0.0.0",
        https: false, //是否为https 请求 https:{type:Boolean}
        proxy:{
          '/api':{
            //target: process.env.VUE_APP_URL, //可以根据不同环境有不同的接口域名
              target:'http://43.138.47.53:5000',// 固定的域名
              changOrigin:true, //允许跨域 
              pathRewrite:{
                  "^/api":"" /* 重写路径，当我们在浏览器中看到请求的地址为：http://localhost:8080/api/core/getData/userInfo 时
                  实际上访问的地址是：http://121.121.67.254:8185/core/getData/userInfo,因为重写了 /api
                 */
              }
          }
      }
  }
}
