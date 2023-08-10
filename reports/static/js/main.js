import * as echarts from 'echarts';

/* const getOptionsChart=async()=>{
    try{
        const response = await fetch("/reports/api/");
        return await response.json();
    }catch (ex){
        alert(ex)
    }
} */

const getOptionsChart=()=>{
    return {
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            data: [
              120,
              {
                value: 200,
                itemStyle: {
                  color: '#a90000'
                }
              },
              150,
              80,
              70,
              110,
              130
            ],
            type: 'bar'
          }
        ]
      };
}


const initChart=()=>{
    var chartDOM = document.getElementById('chart')
    var mychart = echarts.init(chartDOM);
    var option = getOptionsChart();
    option && mychart.setOption(option);
   
};

window.addEventListener("load", () => {
    initChart();
});