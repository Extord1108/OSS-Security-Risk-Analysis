<template>
  <div :id="id" :style="style"></div>
</template>

<script>
import * as echarts from 'echarts'

const idGen = () => {
  return new Date().getTime()
}

//let myChart = null;

export default {
  props: {
    height: {
      type: String,
      default: '500px'
    },
    width: {
      type: String,
      default: '500px'
    },

    options: {
      type: Object,
      default: null
    },
    id: {
      type: String,
      default: null
    }
  },

  data() {
    return {
      uuid: null,
      myChart: null
    }
  },

  watch: {
    width() {
      if (this.myChart != null) {
        setTimeout(() => {
          this.myChart.resize({
            animation: {
              duration: 400
            }
          }
          )
        }, 0);
      }
    },
    options() {
      if (this.myChart != null) {
        this.myChart.setOption(
          this.options, {
          notMerge: true
        }
        )
      }
    }
  },

  computed: {
    // 绑定计算属性style
    style() {
      return {
        height: this.height,
        width: this.width
      }
    }
  },

  created() {
    this.uuid = idGen()
  },

  mounted() {
    setTimeout(() => {
      // 准备实例
      if (echarts.getInstanceByDom(document.getElementById(this.id)) == null) {
        this.myChart = echarts.init(document.getElementById(this.id));
        // 应用配置项
        this.myChart.setOption(this.options);
      }
    }, 1000);
  }
}
</script>

<style scoped>

</style>