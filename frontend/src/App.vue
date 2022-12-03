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
              <!-- <el-dropdown-menu slot="dropdown" style="width: 750px" v-if="showPrefix">
                <el-dropdown-item
                    v-for="item in results"
                    :key="item"
                    :command="item"
                    v-html="highlight(item)">
                </el-dropdown-item>
              </el-dropdown-menu> -->
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
              <el-col :span="6" style="padding: 10px; margin-right: 20px">
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
              <el-col :span="6" style="padding: 10px; margin-right: 20px">
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
              <el-col :span="6" style="padding: 10px; margin-right: 20px">
                <img class="image" src="./assets/images/home_aut.jpg" style="width:70px"/>
              </el-col>
              <el-col :span="6" style="padding: 10px; margin-left: 20px">
                <h3 class="sub-title">恶意包数量</h3>
                <h2 class="sub-number">{{ statistic.mal_count }}</h2>
              </el-col>
            </el-row>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="grid-content bg-purple test_a">
            <el-row>
              <el-col :span="6" style="padding: 10px; margin-right: 20px">
                <img class="image" src="./assets/images/home_org.jpg" style="width:70px"/>
              </el-col>
              <el-col :span="6" style="padding: 10px; margin-left: 20px">
                <h3 class="sub-title">维护者数量</h3>
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
            <div @mouseenter="mouseOver" @mouseleave="mouseLeave">
              <MyCharts id="chart1" :options="options" :width="width"></MyCharts>
            </div>
            <!--<el-button type="primary" @click="changeOpt">changeOpt</el-button>-->
          </el-col>
          <el-col :span="9">
            <MyCharts id="chart2" :options="reflect_options"></MyCharts>
          </el-col>
        </el-card>
      </div>
    </main>
  </div>
</template>

<script>
import axios from "axios";
import MyCharts from "./components/MyCharts.vue";
import { options1, options2, options3, options4 } from "./options";
import PackageBasicInfo from "./components/PackageBasicInfo.vue";
import PackageRiskInfo from "./components/PackageRiskInfo.vue";
import AuthorInfo from "./components/AuthorInfo.vue";

export default {
  name: "App",
  components: {
    MyCharts, PackageBasicInfo, PackageRiskInfo, AuthorInfo
  },
  data() {
    return {
      options: options1,
      reflect_options: options3,
      width: "600px",
      statistic: {
        tot_count: "1104",
        desert_count: "17",
        mal_count: "12",
        maintainer: "943",
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
      selected: true,
      showPackage: true,
      activeNameOut1: "basicInfo1",
      activeNameOut2: "basicInfo2",
      showAuthor: true,
      results: " ",
      info: "",

      package_basic_info: {
        package_name: "element-ui",
        authors: ["vigilant-perlmanstv", "shi_logic"],
        abstract: "Element-Ul是国内饿了么前端团队为开发者、设计师和产品经理推出的基于 Vue 2.0 的桌面端组件库, Element的视觉设计更符合国人的观赏体验, 目前在国内使用的普及率，覆盖率，认知度是相当高的，生态已经基本全覆盖。",
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
    mouseOver() {
      this.changeWidth();
    },

    mouseLeave() {
      this.changeWidth();
    },

    changeWidth() {
      if(this.width == "600px") {
        //console.log(1)
        this.width = "800px";
      } else {
        //console.log(2)
        this.width = "600px";
      }
    },
    changeOpt() {
      if(this.options == options1) {
        this.options = options2;
        this.reflect_options = options4;
      } else {
        this.options = options1;
        this.reflect_options = options3;
      }
    },

    getInfo() {
      axios.post("/cal_human").then((res) => {
        console.log(res);
        if(res != null) {
          let dang = parseInt(res.data.split("/")[0]);
          let total = parseInt(res.data.split("/")[1]);
          this.options.series[0].data[0].value = total - dang;
          this.options.series[0].data[1].value = dang;
        }
      });
      axios.post("/cal_package").then((res) => {
        console.log(res);
        if(res != null) {
          let dang = parseInt(res.data.split("/")[0]);
          let total = parseInt(res.data.split("/")[1]);
          this.reflect_options.series[0].data[0].value = total - dang;
          this.reflect_options.series[0].data[1].value = dang;
          //this.statistic.desert_count = res.data;
        }
      });
    },

    goSearch: function () {
      if (this.searchValue === "") {
        this.info = "error";
        this.selected = true;
        this.results = "请输入包名";
      } else {
        console.log(this.searchValue);
        axios.post("/check_package", { package_id: this.searchValue }).then((res) => {
            console.log(res);
            this.selected = true;
            if (res.data === "No maintainer") {
              this.info = "warning";
              this.results = "搜索结果：当前包未收录";
            } 
            else if (res.data == 1) {
              this.info = "error";
              this.results = "搜索结果：当前包存在维护者域名过期风险";
            } 
            else {
              this.info = "success";
              this.results = "搜索结果：当前包可信";
            }
          });
      }
    },

    close_result() {
      this.selected = false;
    },
  },


  created() {
    this.getInfo();
  },

  mounted() {
    this.options = options1;
    this.reflect_options = options3;
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