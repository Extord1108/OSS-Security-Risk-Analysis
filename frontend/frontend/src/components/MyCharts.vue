<template>
  <div :id="uuid" :style="style"></div>
</template>

<script>
import * as echarts from 'echarts'

const idGen = () => {
  return new Date().getTime()
}

export default {
  props: {
    height: {
      type: String,
      default: '300px'
    },
    width: {
      type: String,
      default: '400px'
    },

    options: {
      type: Object,
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
      if(this.myChart != null) {
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
      if(this.myChart != null) {
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
    // 准备实例
    this.myChart = echarts.init(document.getElementById(this.uuid));
    // 应用配置项
    this.myChart.setOption(this.options);
  }
}
</script>

<style scoped>

</style>