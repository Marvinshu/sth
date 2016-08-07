option = {
    title : {
        text: "",
        subtext: '',
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: ['微博热点','百度文库','百度知道','天涯论坛','爱奇艺','优酷','腾讯视频']
    },
    series : [
        {
            name: '访问来源',
            type: 'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data: [],
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
}

$.only_ajax({
    url: "/j/cata",
    data: {cata: 'cata1'}
    success: (r)->
        myChart = echarts.init(document.getElementById("flot-pie-chart-cata1"))
        option.series[0].data = r.li
        option.title.text = r.cata
        myChart.setOption(option)
})

$.only_ajax({
    url: "/j/cata",
    data: {cata: 'cata2'}
    success: (r)->
        myChart = echarts.init(document.getElementById("flot-pie-chart-cata2"))
        option.series[0].data = r.li
        option.title.text = r.cata
        myChart.setOption(option)
})

$.only_ajax({
    url: "/j/cata",
    data: {cata: 'cata3'}
    success: (r)->
        myChart = echarts.init(document.getElementById("flot-pie-chart-cata3"))
        option.series[0].data = r.li
        option.title.text = r.cata
        myChart.setOption(option)
})

$.only_ajax({
    url: "/j/cata",
    data: {cata: 'cata4'}
    success: (r)->
        myChart = echarts.init(document.getElementById("flot-pie-chart-cata4"))
        option.series[0].data = r.li
        option.title.text = r.cata
        myChart.setOption(option)
})

$.only_ajax({
    url: "/j/cata",
    data: {cata: 'cata5'}
    success: (r)->
        myChart = echarts.init(document.getElementById("flot-pie-chart-cata5"))
        option.series[0].data = r.li
        option.title.text = r.cata
        myChart.setOption(option)
})



$("#btn-mod").click ->
    li = Array()
    $(".txt-mod").each ->
        val = $(this).val()
        if val
            id = $(this).attr('id')
            li.push({'id': id, 'val': val})

    if li.length > 0
        $.only_ajax({
            url: "/j/view/add"
            data: {li: JSON.stringify(li)}
            success: (r)->
                $.tip '修改成功！'
        })
