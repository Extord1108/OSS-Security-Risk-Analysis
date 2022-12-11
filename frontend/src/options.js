let test_msg1 = "包活跃度分析";
let test_msg2 = "许可证分析";
let test_msg3 = "是否提供仓库";
let test_msg4 = "域名过期维护者";
let test_msg5 = "含过期维护者的包";

import {npmDependencies} from "./views/npmDependencies.js"

export const options1 = {
  title: {
    text: test_msg1,
  },
  tooltip: {},
  legend: {
    data: ["数量"],
  },
  xAxis: {
    data: ["活跃", "一般", "不活跃"],
  },
  yAxis: {},
  series: [
    {
      name: "数量",
      type: "bar",
      data: [
        { value: 24105, name: "活跃" },
        { value: 11822, name: "一般" },
        { value: 20908, name: "不活跃"}
      ],
    },
  ],
};

export const options2 = {
  legend: {
    data: ["无许可证", "宽松许可证", "严格许可证"],
  },
  title: {
    text: test_msg2,
  },
  series: [
    {
      type: "pie",
      radius: ["45%", "70%"],
      avoidLabelOverlap: false,
      itemStyle: {
        borderRadius: 10,
        borderColor: '#fff',
        borderWidth: 2
      },
      label: {
        show: false,
        position: "center",
      },
      labelLine: {
        show: false,
      },
      emphasis: {
        label: {
          show: true,
          fontSize: "20",
          fontWeight: "bold",
        },
      },
      data: [
        { value: 614, name: "无许可证" },
        { value: 25558, name: "宽松许可证" },
        { value: 30663, name: "严格许可证"}
      ],
    },
  ],
};


export const options3 = {
  title: {
    text: test_msg3,
  },
  tooltip: {},
  legend: {
    data: ["数量"],
  },
  xAxis: {
    data: ["提供仓库", "不提供仓库"],
  },
  yAxis: {},
  series: [
    {
      name: "数量",
      type: "bar",
      data: [
        { value: 24105, name: "提供仓库" },
        { value: 11822, name: "不提供仓库" },
      ],
    },
  ],
};

export const options4 = {
  legend: {
    orient: "vertical",
    x: "left",
    data: ["风险1", "风险2", "风险3", "风险4", "风险5"],
  },
  xAxis: {
    type: "category",
    data: ["2020", "2021", "2022"],
  },
  yAxis: {
    type: "value",
  },
  series: [
    {
      data: [43.3, 85.8, 93.7],
      type: "line",
    },
    {
      data: [83.1, 73.4, 55.1],
      type: "line",
    },
    {
      data: [86.4, 65.2, 82.5],
      type: "line",
    },
    {
      data: [72.4, 53.9, 39.1],
      type: "line",
    },
  ],
};

export const options7 = {
  title: {
    text: 'NPM 依赖关系'
  },
  animationDurationUpdate: 1500,
  animationEasingUpdate: 'quinticInOut',
  series: [
    {
      type: 'graph',
      layout: 'none',
      // progressiveThreshold: 700,
      data: npmDependencies.nodes.map(function (node) {
        return {
          x: node.x,
          y: node.y,
          id: node.id,
          name: node.label,
          symbolSize: node.size,
          itemStyle: {
            color: node.color
          }
        };
      }),
      edges: npmDependencies.edges.map(function (edge) {
        return {
          source: edge.sourceID,
          target: edge.targetID
        };
      }),
      emphasis: {
        focus: 'adjacency',
        label: {
          position: 'right',
          show: true
        }
      },
      roam: true,
      lineStyle: {
        width: 0.5,
        curveness: 0.3,
        opacity: 0.7
      }
    }
  ]
};