<template>
  <div class="package-risk">
    <div style="text-align:left;">
      <span class="package-name" >包名：{{ packageRiskInfo.package_name }}</span>
    </div>      
    <div style="padding-top:10px;">
      <el-descriptions :column="2" border>
        <el-descriptions-item 
          label="维护者域名是否过期：" 
          label-class-name="my-label" 
          :contentStyle="{'text-align': 'center'}"
          content-class-name="my-content">
          <el-tag size="larger" style="font-size:larger">
            {{ packageRiskInfo.maintainer_overdue == true ? "是" : "否" }}
          </el-tag>
        </el-descriptions-item>
        <el-descriptions-item label="当前包是否安装脚本：" :contentStyle="{'text-align': 'center'}">
          <el-tag size="larger" style="font-size:larger">
            {{ packageRiskInfo.scripts_equipped == true ? "是" : "否" }}
          </el-tag>
        </el-descriptions-item>
        <el-descriptions-item label="代码仓库地址：" :contentStyle="{'text-align': 'center'}">
          <el-tag size="larger" style="font-size:larger">
            {{ packageRiskInfo.repository }}
          </el-tag>
        </el-descriptions-item>
        <el-descriptions-item label="最近维护：" :contentStyle="{'text-align': 'center'}">
          <el-tag size="larger" style="font-size:larger">
            {{ packageRiskInfo.recent_mantainances }}
          </el-tag>
        </el-descriptions-item>
        <el-descriptions-item label="与该包名称相似的恶意包：" :contentStyle="{'text-align': 'center'}">
          <span v-for="(j) in packageRiskInfo.confusing_malpackages" :key="j" class="malpackages-list"> 
            <el-popover
                placement="top-start"
                title="相似度"
                width="100"
                trigger="hover"
                @show="showPopver(packageRiskInfo.package_name, j)"
                :content="similarity.toFixed(6)">
                <el-tag size="larger" style="font-size:larger" slot="reference" >{{ j }}</el-tag>
            </el-popover>
          </span>
        </el-descriptions-item>
        <el-descriptions-item label="许可证:" :contentStyle="{'text-align': 'center'}">
          <el-tag size="larger" style="font-size:larger">
            {{ packageRiskInfo.license }}
          </el-tag>
        </el-descriptions-item>
      </el-descriptions>
    </div>
  </div>
</template>
  
<script>
export default {
  name: "PackageRiskInfo",
  props: ["packageRiskInfo"],
  data() {
    return {
      similarity: 0.0000000,
    }
  },
  methods: {
    showPopver(name, fakeName) {
      this.similarity_cal(name, fakeName);
    },
    roundFun(value, n) {
      return Math.round(value*Math.pow(10,n))/Math.pow(10,n);
    },
    similarity_cal(str1, str2) {
      let len1 = str1.length;
      let len2 = str2.length;
      let diff = new Array(len1 + 1);
      for(let i = 0; i <= len1; i++) {
        diff[i] = new Array(len2 + 1);
      }
      for(let i = 0; i <= len1; i++) {
        diff[i][0] = i * 1.0;
      }
      for(let i = 0; i <= len2; i++) {
        diff[0][i] = i * 1.0;
      }
      let tmp;
      for(let i = 1; i <= len1; i++) {
        for(let j = 1; j <= len2; j++) {
            if(str1[i - 1] === str2[j - 1]) tmp = 0.0;
            else tmp = 1.0;
            let t1 = diff[i - 1][j - 1] + tmp;
            let t2 = diff[i][j - 1] + 1;
            let t3 = diff[i - 1][j] + 1;
            diff[i][j] = t1 < t2 ? (t1 < t3 ? t1 : t3) : (t2 < t3 ? t2 : t3);
        }
      }
      this.similarity = this.roundFun(5/5, 6) - this.roundFun((diff[len1][len2] / Math.max(len1, len2)), 6);
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
</style>