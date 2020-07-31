$(function(){
   Ispr();
   Isprmenu();
})

function Ispr(){
    var swiper=new Swiper("#topswiper",{
        loop:true,
        autoplay:3000,
        pagination:".swiper-pagination"
    });
}

function Isprmenu(){
    var swiper=new Swiper('#swiperMenu',{
        slidesPerView: 3,
    })
}