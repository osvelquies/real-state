    function modifyText() {  
       var livearea = document.getElementsByName("living_area");
        
     //  alert(el[0].value);
     //  alert(livearea[0].value);
       if(parseFloat(el[0].value))
       {
           // alert("1");
            livearea[0].value = parseFloat(el[0].value )+ 10;
           // alert("2");
            var event = new Event('input');
            livearea[0].dispatchEvent(event);
           // livearea[0].input();
           // alert("3");
            event = new Event('keydown');
            livearea[0].dispatchEvent(event);
           // alert("4");
       }
    }
    function soloNumeros(e){
        var key = window.event ? e.which : e.keyCode;
        if ((key < 48 || key > 57)&& key!= 46) {
            e.preventDefault();
        }
    }

    var el = document.getElementsByName('garden_area');
        if(el[0] != null)
        {
            
            el[0].addEventListener("change", modifyText, false); 
            el[0].addEventListener("keypress", function(){ 
                return soloNumeros(event);
                }, false);
        }
     var contenedor = document.getElementsByClassName("PruebaOSM");
     
    contenedor[0].addEventListener("click", tablechange, false); 
    function tablechange ()
    {
        var table2 =  contenedor[0].getElementsByClassName("o_list_table table");
        var renglon2 = table2[0].rows[0];
        var columnas2 = renglon2.getElementsByClassName("Numeradores");
        var columnassort = renglon2.getElementsByClassName("o_column_sortable");

        if(columnas2[0] == null)
        {
            agregarColumnaContador();

        }
    }
    function agregarColumnaContador()
    {
        var table =  contenedor[0].getElementsByClassName("o_list_table table");
        var columnas = table[0].getElementsByClassName("o_column_sortable ");
        var numcon= 0;
        for (var i = 0, row; row = table[0].rows[i]; i++) {
            //alert(row.innerText);
            if(row.innerText.trim() !="" && row.innerText.trim() !="Add a line" )
            {
                if(numcon ==0)
                {
                    var celda = document.createElement("th");
                    celda.id = "Numerador"
                    celda.className="Numeradores"
                    celda.title="Núm."
                    celda.width="50px"
                    //var textoCelda = document.createElement("span");
                    //celda.appendChild(textoCelda);
                    row.insertBefore(celda,row.childNodes[0]);
                }
                else
                {
                    
                    var celda = document.createElement("td");
                    celda.width="50px"
                    celda.class="o_data_cell o_field_cell o_list_number"
                    var textoCelda = document.createElement("p");
                    textoCelda.innerText = numcon;
                    textoCelda.style="text-align : right";
                    celda.appendChild(textoCelda);
                    row.insertBefore(celda,row.childNodes[0]);
                }
                numcon++;
            }
        }
    }
    agregarColumnaContador();
    // // Creamos un array vacio
    // var ElementosClick = new Array();
    // // Capturamos el click y lo pasamos a una funcion
    
    // function captura_click(e) {
    //     // Funcion para capturar el click del raton
    //     var HaHechoClick;
    //     if (e == null) {
    //         // Si hac click un elemento, lo leemos
    //         HaHechoClick = event.srcElement;
    //     } else {
    //         // Si ha hecho click sobre un destino, lo leemos
    //         HaHechoClick = e.target;
    //     }
    //     // Añadimos el elemento al array de elementos
    //     ElementosClick.push(HaHechoClick);
    //     // Una prueba con salida en consola
    //     console.log("Contenido sobre lo que ha hecho click: "+ElementosClick.className);    
    // }
    // document.addEventListener("click", captura_click, false); 
    
    

// odoo.define('estate.javascript',function(require){
//     'use strict';
//     require('web.dom_ready');
//     var core = require('web.core');
//     var session = require('web.session');
//     var SystrayMenu = require('web.SystrayMenu');
//     var Widget = require('web.Widget');5
//     var form_widget = require('web.FormRenderer');
//     var widgetRegistry = require('web.widget_registry');
//     alert('hola mundo');
    
//     var changeTitle = function() {
        
//         //opp_name.value = value_input;
//         alert("funcion");
        
//     };
//     var MyWidget = Widget.extend({

//         template: 'sigPad',
    
//         events: {
//             'click .your_class': 'change_opp_name',
//         },
    
//         change_opp_name: function () {
//             // var opp_name = document.getElementById("value_input");
//             // var value_input = 8;
//              var change_opp_name_button = document.getElementById('boton');
//              var event = new Event('change');
//             change_opp_name_button.addEventListener('change', changeTitle(), false);
//             opp_name.dispatchEvent(event);
//         }
//     });
//     widgetRegistry.add(
//      'my_widget', MyWidget
//     );

//     return MyWidget;
    // 
    // var SideBar = Widget.extend({
    //     init: function (parent) {
    //         this._super.apply(this, arguments);
    //         $('#boton').text="pruebas";
    //     },
    // });
    // return SideBar;


    // form_widget.include({
         
    //     _addOnClickAction: function ($el, node) {

           
    //         var self = this;

    //         $el.click(function () {



    //             if(node.attrs.id === "boton")
    //                 {
                        
    //                     alert(node.attrs.text);
    //                     alert(node.name);
    //                     node.attrs.text = "prueba";
                        
    //                 }

    //               //just code old may use super

    //             self.trigger_up('button_clicked', {

    //                 attrs: node.attrs,

    //                 record: self.state,

    //             });

    //         });

    //     },


    // });


    
//});


/*
 alert('Hola Mundo');
 var rpc = require('web.rpc')
 var Widget = require('web.Widget');
var core = require('web.core');
var _t = core._t;
var QWeb = core.qweb;
var form_common = rpc.form_common;
var formats = rpc.formats;
var form_widget = rpc.form_widgets;
*/


    // var framework = require('web.framework');
    // var form_widget = require('web.FormRenderer');
    // var rpc = require('web.rpc');
    
    // var ajax = require('web.ajax');
    
    // alert("Hola Mundo ");
    // form_widget.include({

        

    //     _addOnClickAction: function ($el, node) {

           
    //         var self = this;

    //         $el.click(function () {


    //             if(node.attrs.id === "boton")
    //                 {
    //                    alert($el.toString());
    //                    node.attrs.text = "prueba";
                    
    //                 var inputNombre = $("#boton");
    //                 alert(inputNombre.name);

    //                 }

    //               //just code old may use super

    //             self.trigger_up('button_clicked', {

    //                 attrs: node.attrs,

    //                 record: self.state,

    //             });

    //         });

    //     },



    // });
