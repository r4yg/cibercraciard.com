var chart = ""

$(function () {
    "use strict";

    var data = {
        labels: [],
        series: [
            [],
            []
        ],
        plugins: [
            Chartist.plugins.tooltip()
        ]
    };

    var options = {
        seriesBarDistance: 12,
        height: "250px",
        fullWidth: true
    };

    var responsiveOptions = [
        ['screen and (min-width: 641px) and (max-width: 1024px)', {
                seriesBarDistance: 10,
                axisX: {
                    labelInterpolationFnc: function (value) {
                        return value;
                    }
                }
            }],
        ['screen and (max-width: 640px)', {
                seriesBarDistance: 10,
                axisX: {
                    labelInterpolationFnc: function (value) {
                        return value;
                    }
                }
            }]
    ];

    chart = new Chartist.Bar('.ct-chart', data, options, responsiveOptions);
    setTimeout(function(){
        location.reload();
    }, 300000)
    update_data();

});

function update_data(){
    var url = "/get_dashboard/";
        $.ajax({
            url: url, type: 'get', datatype: 'json',
            success: function(data){
 
                var vars = {
                    dirigentes_qtt:    data.total_dirigentes,
                    colaboradores_qtt: data.total_colaboradores,
                    seguidores_qtt:    data.total_seguidores,
                    vot_emit : data.total_votos_emitidos,
                    vot_emit_porc : data.total_votos_emitidos_porciento,
                    vot_fal : data.total_votos_faltantes,
                    vot_fal_porc: data.total_votos_faltantes_porciento,
                    total_votantes : data.total_votantes,
                }
                


                $("#dirigentes_qtt").html(vars.dirigentes_qtt);
                $("#colaboradores_qtt").html(vars.colaboradores_qtt);
                $("#seguidores_qtt").html(vars.seguidores_qtt);

                $("#vot_emit").html(vars.vot_emit);
                $("#vot_emit_porc").html(vars.vot_emit_porc);
                $("#vot_fal").html(vars.vot_fal);
                $("#vot_fal_porc").html(vars.vot_fal_porc);

                var labels = [];
                var series = [[],[]];
                var mesas_len = data.mesas.length;
                for(var i = 0; i < mesas_len; i++){
                    labels.push(data.mesas[i].mesa)
                    series[0].push(data.mesas[i].total_votos_emitidos)
                    series[1].push(data.mesas[i].total_votantes)
                }

                var chart_data = {
                    labels: labels,
                    series: series,
                    plugins: [
                        Chartist.plugins.tooltip()
                    ]
                };
                chart.update(chart_data)



                // renderizando el detalle de las mesas
                var template = $('#mesa_template').html();
                Mustache.parse(template);
                var mesas_length = data.mesas.length;
                $('#detalle_mesas').html("");
                for(var i = 0; i < mesas_length; i++){
                    // verificando el porciento para cuadrar el color
                    data.mesas[i].porciento = Math.round((data.mesas[i].total_votos_emitidos / data.mesas[i].total_votantes)*10000)/100
                    
                    if (data.mesas[i].porciento < 15){

                        data.mesas[i].color = "danger";
                    }
                    else if(data.mesas[i].porciento < 30){
                        data.mesas[i].color = "warning";
                    }
                    else if(data.mesas[i].porciento < 45){
                        data.mesas[i].color = "success";
                    }
                    else{
                        data.mesas[i].color = "primary";
                    }

                    $("#detalle_mesas").append(Mustache.render(template, data.mesas[i]));
                }
                setTimeout(function(){
                    update_data()
                }, 3000)


            },
            async: true
        });

}
