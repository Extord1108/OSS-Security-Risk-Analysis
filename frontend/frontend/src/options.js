let test_msg = '风险分析'
export default {
    title: {
        text: test_msg,
    },
    tooltip: {},
    legend: {
        data: ['数量']
    },
    xAxis: {
        data: ["漏洞1", "漏洞2", "漏洞3", "漏洞4", "漏洞5", "漏洞6"]
    },
    yAxis: {},
    series: [{
        name: '数量',
        type: 'bar',
        data: [5, 20, 36, 10, 10, 20]
    }]
};

export const options1 = {
    title: {
        text: test_msg
    },
    tooltip: {},
    legend: {
        data: ['数量']
    },
    xAxis: {
        data: ["漏洞1", "漏洞2", "漏洞3", "漏洞4", "漏洞5", "漏洞6"]
    },
    yAxis: {},
    series: [{
        name: '数量',
        type: 'bar',
        data: [5, 20, 36, 10, 10, 20]
    }]
};

export const options2 = {
    legend: {
        // Try 'horizontal'
        orient: 'vertical',
        right: 0,
        top: 'center'
    },
    title: {
        text: test_msg
    },
    dataset: {
        source: [
            ['product', '2020', '2021', '2022'],
            ['风险1', 43.3, 85.8, 93.7],
            ['风险2', 83.1, 73.4, 55.1],
            ['风险3', 86.4, 65.2, 82.5],
            ['风险4', 72.4, 53.9, 39.1]
        ]
    },
    xAxis: { type: 'category' },
    yAxis: {},
    series: [
        { type: 'bar' }, { type: 'bar' }, { type: 'bar' }
    ]
};

export const options3 = {
    legend: {
        orient: 'vertical',
        x: 'left',
        data: ['漏洞1', '漏洞2', '漏洞3', '漏洞4', '漏洞5']
    },
    series: [{
        type: 'pie',
        radius: ['50%', '70%'],
        avoidLabelOverlap: false,
        label: {
            show: false,
            position: 'center'
        },
        labelLine: {
            show: false
        },
        emphasis: {
            label: {
                show: true,
                fontSize: '20',
                fontWeight: 'bold'
            }
        },
        data: [
            { value: 5, name: '漏洞1' },
            { value: 20, name: '漏洞2' },
            { value: 36, name: '漏洞3' },
            { value: 10, name: '漏洞4' },
            { value: 10, name: '漏洞5' },
            { value: 20, name: '漏洞6' }
        ]
    }]
};

export const options4 = {
    legend: {
        orient: 'vertical',
        x: 'left',
        data: ['风险1', '风险2', '风险3', '风险4', '风险5']
    },
    xAxis: {
        type: 'category',
        data: ['2020', '2021', '2022']
      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          data: [43.3, 85.8, 93.7],
          type: 'line'
        },
        {
            data: [83.1, 73.4, 55.1],
            type: 'line'
        },
        {
            data: [86.4, 65.2, 82.5],
            type: 'line'
        },
        {
            data: [72.4, 53.9, 39.1],
            type: 'line'
        }
      ]
};