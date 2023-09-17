// create a function to display chart 

const displayChart = (labels, data)=>{
    const ctx = document.getElementById('myChart');
new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: labels,
    
     
        
    datasets: [{
      label: "labels",
      data: data,
      backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(54, 162, 235)',
        'rgb(255, 205, 86)'
      ],
    },
   
    ]
  },
  options:{
    plugins:{
        title: {
            display:true,
            text : 'my expenses',
        },
    }
}
});

}

const getChartData = () =>{
    console.log("before fetch");
    fetch('display-chart/display')
    .then((res)=>res.json())
    .then((result)=>{
        // console.log(result.chartdata);
    const chartData = result.chartdata

    const [labels, data] = [Object.keys(chartData), Object.values(chartData)]
    displayChart(labels,data)

    })


}

document.onload = getChartData()