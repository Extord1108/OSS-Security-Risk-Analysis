<template>
  <div>
    <el-header>
      <el-menu class="el-menu-demo" mode="horizontal" background-color="#FFF"
        style="padding-left: 0%; padding-right: 5%">
        <el-menu-item style="font-size: larger; font-weight: 600">风险分析</el-menu-item>

        <div class="input-box-body">
          <div class="input-box">
            <el-dropdown>
              <el-input placeholder="请输入内容" v-model="searchValue" class="input-with-select"
                @keyup.enter.native="goSearch" style="width: 750px; font-size: 17px">
                <el-select v-model="select" slot="prepend" placeholder="检索依据" style="width: 130px">
                  <el-option v-for="item in select_options" :key="item.value" :label="item.label" :value="item.value">
                  </el-option>
                </el-select>
                <el-button slot="append" icon="el-icon-search" @click="goSearch"></el-button>
              </el-input>
              <el-dropdown-menu></el-dropdown-menu>
            </el-dropdown>
          </div>
        </div>

        <div style="float: right">
          <img class="image" src="./assets/images/background2.jpg" style="height: 61px; width: 160px" />
        </div>
      </el-menu>
    </el-header>

    <div class="logos">
      <el-row justify="center" type="flex">
        <el-col :span="6">
          <div class="grid-content bg-purple test_a">
            <el-row>
              <el-col :span="5" style="padding: 10px; margin-right: 20px">
                <img class="image" src="./assets/images/home_art.jpg" style="width:70px"/>
              </el-col>
              <el-col :span="6" style="padding: 10px; margin-left: 20px">
                <h3 class="sub-title">当前总包数</h3>
                <h2 class="sub-number">{{ statistic.tot_count }}</h2>
              </el-col>
            </el-row>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="grid-content bg-purple test_a">
            <el-row>
              <el-col :span="5" style="padding: 10px; margin-right: 20px">
                <img class="image" src="./assets/images/home_fie.jpg" style="width:70px"/>
              </el-col>
              <el-col :span="6" style="padding: 10px; margin-left: 20px">
                <h3 class="sub-title">弃用包数量</h3>
                <h2 class="sub-number">{{ statistic.desert_count }}</h2>
              </el-col>
            </el-row>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="grid-content bg-purple test_a">
            <el-row>
              <el-col :span="5" style="padding: 10px; margin-right: 20px">
                <img class="image" src="./assets/images/home_aut.jpg" style="width:70px"/>
              </el-col>
              <el-col :span="6" style="padding: 10px; margin-left: 20px">
                <h3 class="sub-title">脚本包数量</h3>
                <h2 class="sub-number">{{ statistic.mal_count }}</h2>
              </el-col>
            </el-row>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="grid-content bg-purple test_a">
            <el-row>
              <el-col :span="5" style="padding: 10px; margin-right: 20px">
                <img class="image" src="./assets/images/home_org.jpg" style="width:70px"/>
              </el-col>
              <el-col :span="6" style="padding: 10px; margin-left: 20px">
                <h3 class="sub-title">过期维护者</h3>
                <h2 class="sub-number">{{ statistic.maintainer }}</h2>
              </el-col>
            </el-row>
          </div>
        </el-col>
      </el-row>
    </div>

    <div v-if="selected">
      <el-row justify="center" type="flex">
        <el-col :span="22">
          <div>
            <el-row>
              <el-alert class="results-box" 
                :title="results" 
                :type="info" 
                @close="close_result" 
                style="
                  font-size: larger !important;
                  font-weight: bold !important;
                ">
              </el-alert>
            </el-row>
          </div>

          <div v-if="showPackage" class="infoBox">
            <el-tabs v-model="activeNameOut1">
              <el-tab-pane label="基本信息" name="basicInfo1" style="text-align:left">
                <PackageBasicInfo :packageBasicInfo="package_basic_info"></PackageBasicInfo>
              </el-tab-pane>
              <el-tab-pane label="风险信息" name="riskInfo1" style="text-align:left">
                <PackageRiskInfo :packageRiskInfo="package_risk_info"></PackageRiskInfo>
              </el-tab-pane>
            </el-tabs>
          </div>

          <div v-if="showAuthor" class="infoBox">
            <el-tabs v-model="activeNameOut2">
              <el-tab-pane label="作者信息" name="basicInfo2" style="text-align:left">
                <AuthorInfo :authorInfo="author_info"></AuthorInfo>
              </el-tab-pane>
            </el-tabs>
          </div>
        </el-col>
      </el-row>
    </div>

    <main>
      <div class="container">
        <el-card class="card">
          <el-col :span="15">
            <div @mouseenter="mouseOver1" @mouseleave="mouseLeave1">
              <MyCharts id="chart1" :options="options1" :width="width1"></MyCharts>
            </div>
            <!--<el-button type="primary" @click="changeOpt">changeOpt</el-button>-->
          </el-col>
          <el-col :span="9">
            <MyCharts id="chart2" :options="options2"></MyCharts>
          </el-col>
          <el-col :span="15">
            <div @mouseenter="mouseOver2" @mouseleave="mouseLeave2">
              <MyCharts id="chart3" :options="options3" :width="width2"></MyCharts>
            </div>
            <!--<el-button type="primary" @click="changeOpt">changeOpt</el-button>-->
          </el-col>
          <br/>
          <el-col :span="9">
            <MyCharts id="chart4" :options="options4"></MyCharts>
          </el-col>
          <el-col :span="15">
              <MyCharts id="chart5" :options="options5"></MyCharts>
          </el-col>
          <el-col :span="9">
              <MyCharts id="chart6" :options="options6"></MyCharts>
          </el-col>
          <el-col :span="20">
            <div>
              <MyCharts id="chart7" :options="options7" :width="width7" :height="height7"></MyCharts>
            </div>
          </el-col>
        </el-card>
      </div>
    </main>
  </div>
</template>

<script>
import axios from "axios";
import MyCharts from "./components/MyCharts.vue";
import { options1, options2, options3, options4, options5, options6, options7 } from "./options";
import PackageBasicInfo from "./components/PackageBasicInfo.vue";
import PackageRiskInfo from "./components/PackageRiskInfo.vue";
import AuthorInfo from "./components/AuthorInfo.vue";
import qs from 'qs';

export default {
  name: "App",
  components: {
    MyCharts, PackageBasicInfo, PackageRiskInfo, AuthorInfo
  },
  data() {
    return {
      options1: options1,
      options2: options2,
      options3: options3,
      options4: options4,
      options5: options5,
      options6: options6,
      options7: options7,
      width1: "600px",
      width2: "600px",
      width3: "600px",
      width7: "1500px",
      height7: "900px",
      statistic: {
        tot_count: 0,
        desert_count: 0,
        mal_count: 0,
        maintainer: 0,
        script_package: 0,

      },
      expired_count: {
        expired_package: 0,
        expired_human: 0
      },
      searchValue: "",
      select_options: [
        {
          value: "package_name",
          label: "包名",
        },
        {
          value: "author_name",
          label: "作者",
        },
      ],
      value: "package_name",
      select: "package_name",
      selected: false,
      showPackage: false,
      activeNameOut1: "basicInfo1",
      activeNameOut2: "basicInfo2",
      showAuthor: false,
      results: " ",
      info: "",

      package_basic_info: {
        package_name: "element-ui",
        //authors: ["vigilant-perlmanstv", "shi_logic"],
        license: "MIT license",
        latest_version: "^2.15.10",
      },

      package_risk_info: {
        package_name: "element-ui",
        maintainer_overdue: false,
        scripts_equipped: true,
        recent_mantainances: "2 days ago",
        repository: "https://github.com/element-plus/element-plus",
        confusing_malpackages: ["Element-UI", "elemt-ui", "ele-ui"],
        license: "MIT license",
      },

      author_info: {
        name: "shi_logic",
        email: "2041341499@qq.com",
        personal_site: "https://github.com/shilogic0929",
        maintainer_overdue: true,
        abstract: "Hello World!",
        projects_involved: [
          {proName: 'Re-Li-Life/OSS-Security-Analysis', url: 'https://github.com/Re-Li-fe/OSS-Security-Risk-Analysis'},
          {proName: 'natsunishitagau/sework', url: 'https://github.com/natsunishitagau/sework'}, 
          {proName: 'melonotmelo/rent-manager', url: 'https://github.com/melonotmelo/rent-manger'},
          {proName: 'shilogic0929/MyProject', url: 'https://github.com/shilogic0929/MyProject'},  
        ],
      },

    };
  },
  methods: {
    mouseOver1() {
      this.changeWidth1();
    },
    mouseLeave1() {
      this.changeWidth1();
    },
    mouseOver2() {
      this.changeWidth2();
    },
    mouseLeave2() {
      this.changeWidth2();
    },
    mouseOver3() {
      this.changeWidth3();
    },
    mouseLeave3() {
      this.changeWidth3();
    },
    changeWidth1() {
      if(this.width1 == "600px") this.width1 = "800px";
      else this.width1 = "600px";
    },
    changeWidth2() {
      if(this.width2 == "600px") this.width2 = "800px";
      else this.width2 = "600px";
    },
    changeWidth3() {
      if(this.width3 == "600px") this.width3 = "800px";
      else this.width3 = "600px";
    },
    changeOpt() {
      if(this.options == options1) {
        this.options = options2;
        this.options3 = options4;
      } else {
        this.options = options1;
        this.options3 = options3;
      }
    },

    getInfo() {
      axios.post("/summary").then((res=>{
        if(res.status == 200) {
          this.statistic.tot_count = res.data.package;
          this.statistic.desert_count = res.data.deprecated;
          this.statistic.mal_count = res.data.malicious;
          this.statistic.maintainer = res.data.maintainer
        }
      }))
      axios.post("/cal_expired_human").then((res) => {
        if(res.status == 200) {
          this.expired_count.expired_human = res.data.expired_num;
        }
      });
      axios.post("/cal_expired_package").then((res) => {
        if(res.status == 200) {
          this.expired_count.expired_package = res.data.expired_package_num;
        }
      });
      axios.post("/cal_script").then((res) => {
        if(res.status == 200) {
          this.statistic.script_package = res.data.script_num;
        }
      });
      axios.post("/cal_lazy").then((res) => {
        if(res.status == 200) {
          this.options1.series[0].data[0].value = res.data.over_two;
          this.options1.series[0].data[1].value = res.data.one_to_two;
          this.options1.series[0].data[2].value = res.data.under_one;
        }
      });
      axios.post("/cal_lisence").then((res) => {
        if(res.status == 200) {
          this.options2.series[0].data[0].value = res.data.no_num;
          this.options2.series[0].data[1].value = res.data.easy_num;
          this.options2.series[0].data[2].value = res.data.strict_num;
        }
      });
      axios.post("/cal_res").then((res) => {
        if(res.status == 200) {
          this.options3.series[0].data[0].value = res.data.have_res;
          this.options3.series[0].data[1].value = res.data.no_res;
        }
      });
      axios.post("/cal_expired_human").then((res) => {
        if(res.status == 200) {
          this.options4.series[0].data[0].value = res.data.expired_num;
          this.options4.series[0].data[1].value = res.data.all_human_num - res.data.expired_num;
        }
      });
      axios.post("/cal_expired_package").then((res) => {
        if(res.status == 200) {
          this.options5.series[0].data[0].value = res.data.expired_package_num;
          this.options5.series[0].data[1].value = res.data.all_package_num - res.data.expired_package_num;
        }
      });
      axios.post("/cal_script").then((res) => {
        if(res.status == 200) {
          this.options6.series[0].data[0].value = res.data.script_num;
          this.options6.series[0].data[1].value = res.data.all_num - res.data.script_num;
        }
      });
    },

    goSearch: function () {
      if (this.searchValue === "") {
        this.info = "error";
        this.selected = true;
        this.results = "请输入包名/人名";
      } else {
        if(this.select === "package_name") {
          axios.post("/searchPackage", qs.stringify({ package_id: this.searchValue })).then((res) => {
              this.selected = true;
              if (res.data === "No result") {
                this.info = "error";
                this.showPackage = false;
                this.showAuthor = false;
                this.results = "搜索结果：当前包未收录";
              } 
              else if (res.data.package_expired == 1) {
                this.showPackage = true;
                this.showAuthor = false;
                this.info = "warning";
                this.results = "搜索结果：当前包存在维护者域名过期风险";
                this.package_basic_info.package_name = res.data.name;
                this.package_basic_info.latest_version = res.data.last_version;
                this.package_basic_info.license = res.data.license;

                this.package_risk_info.package_name = res.data.name;
                this.package_risk_info.license = res.data.license;
                this.package_risk_info.latest_version = res.data.last_version;
                this.package_risk_info.maintainer_overdue = true;
                this.package_risk_info.scripts_equipped = res.data.package_script;
                this.package_risk_info.confusing_malpackages = res.data.malicious_package;
                this.package_risk_info.repository = res.data.repository;
                this.package_risk_info.recent_mantainances = res.data.dif_time + ' days ago';
              } 
              else {
                this.showPackage = true;
                this.showAuthor = false;
                this.info = "success";
                this.results = "搜索结果：当前包可信";
                this.package_basic_info.package_name = res.data.name;
                this.package_basic_info.latest_version = res.data.last_version;
                this.package_basic_info.license = res.data.license;

                this.package_risk_info.package_name = res.data.name;
                this.package_risk_info.license = res.data.license;
                this.package_risk_info.latest_version = res.data.last_version;
                this.package_risk_info.maintainer_overdue = false;
                this.package_risk_info.scripts_equipped = res.data.package_script;
                this.package_risk_info.confusing_malpackages = res.data.malicious_package;
                this.package_risk_info.repository = res.data.repository;
                this.package_risk_info.recent_mantainances = res.data.dif_time + ' days ago';
              }
          });
        }
        else {
          axios.post("/searchHuman", qs.stringify({ name: this.searchValue })).then((res) => {
            this.selected = true;
            if (res.data === "No result") {
              this.showPackage = false;
              this.showAuthor = false;
              this.info = "error";
              this.results = "搜索结果：未查到该作者";
            }
            else if(res.data.human_expired == 1) {
              this.showAuthor = true;
              this.showPackage = false;
              this.info = "warning";
              this.results = "该作者域名已过期";
              this.author_info.maintainer_overdue = true;
              this.author_info.name = res.data.name;
              this.author_info.email = res.data.email;
              this.author_info.personal_site = res.data.url;
            } 
            else {
              this.showAuthor = true;
              this.showPackage = false;
              this.info = "success";
              this.results = "该作者域名未过期";
              this.author_info.maintainer_overdue = false;
              this.author_info.name = res.data.name;
              this.author_info.email = res.data.email;
              this.author_info.personal_site = res.data.url;
            }
          });
        }
      }
    },

    close_result() {
      this.selected = false;
      this.showPackage = false;
      this.showAuthor = false;
    },
  },

  created() {
    this.getInfo();
  },

  mounted() {

  },

  watch: {
    // searchValue(newVal, oldVal) {
    //   if(newVal !== '' && newVal !== oldVal)
    //     this.getPrefix();
    // },
    // select(newVal, oldVal) {
    //   if (newVal !== '' && newVal !== oldVal)
    //     this.getPrefix();
    // },
  },
};
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: Helvetica, "PingFang SC", "Microsoft Yahei", sans-serif;
}

.input-box-body {
  float: right;
  padding-top: 10px;
  padding-left: 7%;
  padding-right: 10%;
  text-align: left;
}

.logos {
  margin-top: 10px;
  padding-top: 0px;
  padding-left: 5%;
  background: linear-gradient(to bottom,
      rgba(238, 230, 230, 0.424) 10%,
      rgba(245, 245, 245, 0.15) 100%),
    radial-gradient(at top center, rgba(255, 255, 255, 0.4) 0%, #acacc1 120%) #989898;
  background-blend-mode: multiply, multiply;
}

.sub-title {
  display: block;
  font-family: "Courier New", serif;
  font-weight: bold;
  margin-bottom: 0 !important;
  color: white;
}

.sub-number {
  display: block;
  font-family: "Courier New", serif;
  margin-top: 10px;
  color: white;
}

/* 整个页面 */
main {
  width: 100vw;
  min-height: 100vh;
  padding: 5px 5px;
  display: grid;
  align-items: start;
  justify-items: left;
  background: #969698;
}

/* 容器 */
.container {
  width: 100%;
  height: 100%;

  box-shadow: 0px 0px 24px rgba(0, 0, 0, 0.15);
  padding: 20px 25px;
  background-color: rgb(245, 246, 252);
}

.test_a {
  display: block;
  margin: 0 auto;
  width:100%;
  overflow: hidden;
}

.test_a img {
  width: 100%;
  transform: scale(1);
  transition: all 0.7s ease 0s;
}

.test_a:hover img {
  transform: scale(1.2);
  transition: all 0.7s ease 0s;
}

.card {
  padding: 0 0 10px 0;
}

.el-tabs__item.is-active{
  color: #00b1fd;
  font-weight: 650;
}

.el-tabs__active-bar{
  transition: all 0.5s;
  background-color: #00b1fd;
}

.infoBox {
  margin: 10px 2%;
  padding: 5px 10px 10px;
  background-color: white;
  box-shadow: 0 4px 4px rgba(0, 0, 0, .08), 0 0 6px rgba(0, 0, 0, .04);
}

</style>