let test_msg1 = "包活跃度分析";
let test_msg2 = "许可证分析"

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
    // Try 'horizontal'
    orient: "vertical",
    right: 0,
    top: "center",
  },
  title: {
    text: test_msg1,
  },
  dataset: {
    source: [
      ["product", "2020", "2021", "2022"],
      ["风险1", 43.3, 85.8, 93.7],
      ["风险2", 83.1, 73.4, 55.1],
      ["风险3", 86.4, 65.2, 82.5],
      ["风险4", 72.4, 53.9, 39.1],
    ],
  },
  xAxis: { type: "category" },
  yAxis: {},
  series: [{ type: "bar" }, { type: "bar" }, { type: "bar" }],
};

export const options3 = {
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
