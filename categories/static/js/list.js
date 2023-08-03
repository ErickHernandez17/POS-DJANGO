var contenedor = document.getElementById('category_list');
const list_elements = async() => {
    try{
        const response = await fetch("./categories");
        const data = await response.json();
        
        if (data.message == "Success"){
            var opciones = ``;
            data.categories.forEach((category)=>{
                opciones+=`<li class="list-group-item d-flex justify-content-between align-items-center generic-item">${category.category}
                <div>
                    <a class="btn btn-primary btn-sm open-popup" data-update-url="/category/update/${category.id}" %}">Editar</a>
                    <a class="btn btn-danger btn-sm delete-category" data-category-id="${category.id}">Eliminar</a>
                </div>
                </li>
               `
            });
            contenedor.innerHTML = opciones;
        }else{
            alert("Error al obtener las categorias")
        }

    }catch(error){
        console.log(error);
    }
}


const cargaInicial = async() => {
    await list_elements();
}


window.addEventListener("load", async() =>{
    await cargaInicial();
});

$(document).ready(function() {
    // Delegación de eventos para los botones de "Editar"
    $(document).on("click", ".open-popup", function(event) {
      event.preventDefault();
      var url = $(this).data("update-url");
      var popup = window.open(url, "Editar Categoria", "width=800,height=600");
        console.log('ventana abierta');
      popup.updateUrl = $(this).data("update-url");
    });
  
    // Escuchar el evento de mensaje desde la ventana emergente
    window.addEventListener('message', function(event) {
      if (event.data.action === 'popupClosed' && event.data.message === 'Success') {
        // Actualizar la lista de categorías
        console.log('Se cerró la ventana de edición');
        list_elements();
      }
    });
  });
  

  $(document).ready(function() {
    // Delegación de eventos para los botones de "Eliminar"
    $(document).on("click", ".delete-category", function(event) {
        event.preventDefault();
        var categoryId = $(this).data("category-id");
        
        // Mostrar ventana emergente de confirmación
        var confirmDelete = confirm("¿Estás seguro de que deseas eliminar esta categoría?");
        
        if (confirmDelete) {
            // Realizar la eliminación
            deleteCategory(categoryId);
        }
    });

});

function deleteCategory(categoryId) {
    $.ajax({
        url: `/category/delete/${categoryId}/`,  // Cambia la URL según tu configuración
        type: "POST",
        data: { csrfmiddlewaretoken: "{{ csrf_token }}" },  // Agrega el token CSRF
        success: function(data) {
            if (data.message === "success") {
                // Actualizar la lista de categorías
                list_elements();
            } else {
                alert("Error al eliminar la categoría");
            }
        }
    });
}

  
  