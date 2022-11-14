<template>
  <div>
    <el-header>
      <el-menu
        class="el-menu-demo"
        mode="horizontal"
        background-color="#FFF"
        style="padding-left: 0%; padding-right: 5%;">
        <el-menu-item>风险分析</el-menu-item>

        <div class="input-box-body">
          <div class="input-box">
            <el-dropdown @command="handleCommand" trigger="click" placement="bottom">
              <el-input placeholder="请输入内容"
                        v-model="searchValue"
                        class="input-with-select"
                        @keyup.enter.native="goSearch"
                        style="width: 750px; font-size: 17px"
              >
                <el-select v-model="select" slot="prepend" placeholder="检索依据" style="width: 130px" >
                  <el-option
                      v-for="item in select_options"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value">
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
            </el-dropdown>
          </div>
        </div>

        <div style="float:right;">
          <img class="image" src="./assets/images/background2.jpg" style="height:61px; width:160px">
        </div>
      </el-menu>
    </el-header>

    <div class="logos">
      <el-row gutter="0" justify="center" type="flex">
        <el-col :span="6"><div class="grid-content bg-purple test_a">
          <el-row>
            <el-col :span="6" style="padding:10px; margin-right:20px">
              <img class="image" src="./assets/images/home_org.jpg" :style="imgSize1" @mouseenter="mouseOver1" @mouseleave="mouseLeave">
            </el-col>
            <el-col :span="6" style="padding:10px; margin-left:20px">
              <h3 class="sub-title">当前总包数</h3>
              <h2 class="sub-number">{{ statistic.tot_count }}</h2>
            </el-col>
          </el-row>
        </div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple test_a">
          <el-row>
            <el-col :span="6" style="padding:10px; margin-right:20px">
              <img class="image" src="./assets/images/home_fie.jpg" :style="imgSize2" @mouseenter="mouseOver2" @mouseleave="mouseLeave">
            </el-col>
            <el-col :span="6" style="padding:10px; margin-left:20px">
              <h3 class="sub-title">被弃用包数</h3>
              <h2 class="sub-number">{{ statistic.desert_count }}</h2>
            </el-col>
          </el-row>
        </div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple test_a">
          <el-row>
            <el-col :span="6" style="padding:10px; margin-right:20px">
              <img class="image" src="./assets/images/home_aut.jpg" :style="imgSize3" @mouseenter="mouseOver3" @mouseleave="mouseLeave">
            </el-col>
            <el-col :span="6" style="padding:10px; margin-left:20px">
              <h3 class="sub-title">恶意包数目</h3>
              <h2 class="sub-number">{{ statistic.mal_count }}</h2>
            </el-col>
          </el-row>
        </div></el-col>
      </el-row>
    </div>

    <main>
      <div class="container">
        <el-card class="card">
          <el-col :span="15">
            <div @mouseenter="mouseOver4" @mouseleave="mouseLeave2">
              <MyCharts :options="options" :width="width"></MyCharts>
          </div>
          <el-button type="primary" @click="changeOpt">changeOpt</el-button>
          </el-col>
          <el-col :span="9">
            <MyCharts :options="reflect_options"></MyCharts>
          </el-col>
        </el-card>
      </div>
    </main>
  </div>
</template>

<script>
import MyCharts from './components/MyCharts.vue'
import { options1, options2, options3, options4 } from './options'

export default {
  name: 'App',
  components: {
    MyCharts
  },
  data() {
    return {
      options: options1,
      reflect_options: options3,
      width: '500px',
      imgSize1: "width:70px",
      imgSize2: "width:70px",
      imgSize3: "width:70px",
      statistic: {
        tot_count: '280,050,502',
        desert_count: '16,479',
        mal_count: '49,063'
      },
      searchValue: '',
      select: 'main',
      select_options: [
        {
          value: 'main',
          label: '包名'
        }, {
          value: 'title',
          label: '篇名'
        }, {
          value: 'abstract',
          label: '摘要'
        }, {
          value: 'field',
          label: '领域'
        }, {
          value: 'author_name',
          label: '作者'
        }, {
          value: 'publisher',
          label: '来源'
        }, {
          value: 'doi',
          label: 'DOI'
        },
      ],
      value: '',
      // results: [],
      // showPrefix: true,
    }
  },
  methods: {
    mouseOver1 () {
      this.imgSize1="height:80px;width:90px";
    },
    mouseOver2 () {
      this.imgSize2="height:80px;width:90px";
    },
    mouseOver3 () {
      this.imgSize3="height:80px;width:90px";
    },
    mouseOver4 () {
      this.changeWidth();
    },
 
    mouseLeave () {
      this.imgSize1="width:70px";
      this.imgSize2="width:70px";
      this.imgSize3="width:70px";
    },

    mouseLeave2() {
      this.changeWidth();
    },

    changeWidth() {
      if(this.width == '500px') {
        //console.log(1)
        this.width = '700px'
      } 
      else {
        //console.log(2)
        this.width = '500px'
      }
    },
    changeOpt() {
      if (this.options == options1) {
        this.options = options2
        this.reflect_options = options4
      } 
      else {
        this.options = options1
        this.reflect_options = options3
      }
    },

    goSearch:function() {
      // if (this.searchValue === '') {
      //   this.$message.warning("请输入检索词！");
      //   return;
      // }
      // let routeUrl = this.$router.resolve({
      //   path: '/searchRes?' + this.select + "=" + this.searchValue,
      // });
      // window.open(routeUrl .href, "_self");
    },
  }
}
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
  background: linear-gradient(to bottom, rgba(255,255,255,0.15) 0%, rgba(245, 245, 245, 0.15) 100%), radial-gradient(at top center, rgba(255,255,255,0.40) 0%, #acacc1 120%) #989898; 
  background-blend-mode: multiply,multiply;
}

.sub-title {
  display:block;
  font-family: 'Courier New',serif;
  font-weight:bold;
  margin-bottom:0 !important;
  color:white;
}

.sub-number {
  display:block;
  font-family:'Courier New',serif;
  margin-top:10px;
  color:white;
}

/* 整个页面 */
main {
  width: 100vw;
  min-height: 100vh;
  padding: 10px 10px;
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

.card {
  padding: 0 0 10px 0;
}
</style>