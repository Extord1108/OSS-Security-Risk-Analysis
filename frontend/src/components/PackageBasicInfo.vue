<template>
  <div class="package-basic">
    <div style="text-align:left;">
      <span class="package-name" >包名：{{ packageBasicInfo.package_name }}</span>
    </div>
    <!-- <div style="padding-top:20px;">
      作者：
      <span v-for="(j, idx) in packageBasicInfo.authors" :key="j" class="author-name">{{ j }}
        <span v-if="idx<packageBasicInfo.authors.length-1" style="color: #A0A0A0; font-size: 16px"> / </span>
      </span>
    </div> -->
    <div style="text-align:left;margin-top:20px;">
      许可证：<span class="abstract">{{ packageBasicInfo.license|ellipsis }}</span>
    </div>
    <div style="padding-top:20px">
      <span class="latest-version">最新版本：{{ packageBasicInfo.latest_version }}</span>
    </div>
  </div>
</template>
  
  <script>
  export default {
    name: "PackageBasicInfo",
    props: ["packageBasicInfo"],
    filters: {
      ellipsis: function(value) {
        if(!value) return "";
        if(value.length > 68) {
          return value.slice(0, 68) + "...";
        }
        return value;
      },
    }
  }
  </script>
  
<style scoped>
.package-name {
  font-size: 20px;
  font-weight: 700;
  line-height: 1.4;
  font-family: Tahoma,fantasy;
}
.author-name {
  color: #00b3ff;
  font-size: 16px;
}

.abstract {
    font-family: Georgia, Lato-Regular,Lato,sans-serif;
    font-size: 15px;
    line-height: 22px;
    color: #262625;
}
.latest-version {
  color:grey;
  font-size: 14px;
}
</style>