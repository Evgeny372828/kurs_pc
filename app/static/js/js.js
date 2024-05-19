
var kat=document.getElementById('katalog')
var win_kat=document.getElementById('win_kat')
var wind_p=document.getElementById('wind_p')
var sap=document.getElementById('sap')
var bur=document.getElementById('bur')
var but_sap=document.getElementById('but_sap')
var but_sap1=document.getElementById('but_sap1')
var menu=document.getElementById('menu')
var poisk=document.getElementById('poisk')
var reg=document.getElementById('reg')

bur.addEventListener("click",function(){
        menu.style.display="block",
        poisk.style.display="block",
        reg.style.display="flex"
    }
)


but_sap.addEventListener("click",function(){
    if (sap.style.display=="block"){
        document.getElementById('sap').style.display="none"

    }
    else{
        document.getElementById('sap').style.display="flex"
    }
 }
)
but_sap1.addEventListener("click",function(){
    if (sap.style.display=="block"){
        document.getElementById('sap').style.display="none"
    }
    else{
        document.getElementById('sap').style.display="flex"
    }
 }
)
sap.addEventListener("submit",function(){
        document.getElementById('sap').style.display="none"
    }
)

$('.sli').slick({
  lazyLoad: 'ondemand',
  slidesToShow: 5,
  slidesToScroll: 1
})
function showSubcategories(categoryId) {
  var subcategories = document.getElementsByClassName('subcategories');
  for (var i = 0; i < subcategories.length; i++) {
    subcategories[i].style.display = 'none';
  }

  var selectedCategory = document.getElementById('category-' + categoryId);
  selectedCategory.style.display = 'block';
}

function fetchCategories() {
  fetch('/get_categories/')
    .then(response => response.json())
    .then(data => {
      var categoriesContainer = document.getElementById('categories');

      data.categories.forEach(category => {
        var categoryElement = document.createElement('li');
        categoryElement.innerText = category.name;
        categoryElement.classList.add('category');
        categoryElement.onmouseover = function() {
          showSubcategories(category.id);
        };

        var subcategoriesContainer = document.createElement('ul');
        subcategoriesContainer.classList.add('subcategories');
        subcategoriesContainer.id = 'category-' + category.id;

        data.subcategories.forEach(subcategory => {
          if (subcategory.category_id === category.id) {
            var subcategoryElement = document.createElement('li');
            subcategoryElement.innerText = subcategory.name;
            subcategoriesContainer.appendChild(subcategoryElement);
          }
        });

        categoryElement.appendChild(subcategoriesContainer);
        categoriesContainer.appendChild(categoryElement);
      });
    });
}
const nav = document.querySelector('.nav');
nav.addEventListener('click',(event) => {
    nav.classList.toggle('open');
});
let map;
async function initMap() {

  const position = { lat: -25.344, lng: 131.031 };

  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerView } = await google.maps.importLibrary("marker");


  map = new Map(document.getElementById("map"), {
    zoom: 4,
    center: position,
    mapId: "DEMO_MAP_ID",
  });

  const marker = new AdvancedMarkerView({
    map: map,
    position: position,
    title: "Uluru",
  });
}

initMap();
//fetchCategories();
//$(document).ready(
//  $('#form1').submit(function(e){
//    e.preventDefault();
//    var serializedData = $(this).serialize();
//
//    $.ajax({
//      type:"POST",
//      data:serializedData,
//      success: function(data){
//
//      },
//    });
//  })
//);

//function update_reviews() {
//  $.ajax({
//    url: '/katalog-inform-tovar/3/',
//    type: 'GET',
//    success: function(data) {
//      $('#reviews').html(data);
//    }
//  });
//}
//
//setInterval(update_reviews, 5000);