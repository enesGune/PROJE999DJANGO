# PROJE999DJANGO
--- firstProjectkt ---

    .Bu bir django öğrenme projesi 
    .note sanal ile proje kurmak daha kullanışlıdır 
    .projeyi startlamak için cmd ye --django-admin startproject projectname
    .server başlatmak için --python manage.py run server
    .veri tabanına erişmek ve değişikleri atamak için terminal --python manage.py migrate 



--- setting.py ---

    .BASE_DIR // bu ksımda projeni  bulunduğu dosya yoludur
    .SECRET_KEY // bu ise her django projesinin jendi iinde bir anahtarı bulunur
    .DEBUG // hata ayıklama modu standart True dur
    .ALLOWED_HOSTS // 
    .INSTALLED_APPS // projemizde yüklü olan uygulamar
    .MIDDLEWARE // ara katman güvenliğin ve isteklerin yöneltiği katman dır
    .ROOT_URLCONF // url yönlendirme kısmı
    .TEMPLATES // django HTML şablon kısmı
    .WSGI_APPLICATION // sunucuda çalışma kısmı
    .DATABASES // veri tabanın yönetildiği kısmı
    .AUTH_PASSWORD_VALIDATORS // şifrenin soğrulama ve düzenleme kısmı
    .
    .
    .
    .
    .
    .STATIC_URL // css javascript gibi dosyaların sağlandığı kısmı


--- build-companents ---
    .ilk olarak bri admin oluşturmamız gerekmekte acılan sunucıda/admin yazdığım kısmı kullanabilmek için
    .--python manage.py createsuperuser -- yazdıktan sonra önce kullanıcı adı daha sonra ise email ve passwordu giriyoruz
    .kendi ilk uygulamaız için --python manage.py startapp name
    .oluşturduğumuz model klasmründe models.py a gittik ve buarada veritabanı da ayarları kolonları yazdıktan sonra migrate edicez
    .setting.py a gidip oaradaki app kısmına uygulamızın adını yazıyoruz


--- models.py ---
    .bu dosya veri tabanın yönetmemizi sağlar 
    .models.TextField() bizim varcahar a eşittir
    .yeni bir model yazdığımızda migrate etmek içn cmd ye --python manage.py makemigrations yazarız ardında migrate ederiz
    .

--- admin.py ---
    .modelimport erdiyoruz bu sayede yazdığıız uygulamayı admin panaelinde görüyoruz
    .--python manage.py shell-- bu komut bizim adminde yaptığımız işi cmd de yapmamıza olanak sağlar
    .

--- new-models-field ---
    .modelleri yeniden başlatacağımız ksım

--- default-homepage---custom-homepage ---
    ...views.py... 
        .bu kısım kendi sayfalarımız oluşturduğumuz alan 

--- urls.py ---
    .sayfamızın urlelerini düzenlediğimiz kısım
    .urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
    ] bu kısımda bir oute yaptık 
    ... route-request ...
        path('home/', views.home_view, name='home') bu şekilde route edilebilir

--- views.py ---
    .bu kısm sayfaları oluşturduğumuz ve request ile sasyafadan etkiledşim aldığımız kısmı
    .bu rada kişi doğrulama yapılabilir
    .request,*args**kwargs bizim sayfa etkileşme kodlarımız


--- django-templates --- 
    .bu sayfa şablonları ksımı
    .homepage kısmında render kullanarak yazdığımız html sayfasını geri gönderdik

--- templates ---
    .bu klasor bizim sayfa tasarımlarımızn yani html lerin bulunduğu kısım 
    .kurduktan sonra ayarlardan tamlete de değiiklik yapmamız gerecek
    . {{request.user}} bu bizim djangoda kullandığımız bir methot
    .{{request.user.is_authenticated}} kullanıcı login olup olmadığını sorduk
    .    {% block content %}
        replace me
    {% endblock %}
    böylece bir şablon yapılandırdık ve exdent edeert aynı şablonu sadece içeri değiştirerek kullnabilir hale getirdik
    .{% include 'navbar.html' %} bu şekilde navbar gibi öğereli alabiliypruz
    .viewde abouttaki gibi dataları göstermeye çalışıcaz
    .for ile aboutta listemizinnelemenalarını tek tek döndük {{forloop.counter}} bu ise bir listeyi numaralandırı
    .abouttta yine basit bir if else bloğu kullandık
