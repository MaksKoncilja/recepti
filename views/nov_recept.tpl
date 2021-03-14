% rebase('bootstrap.tpl')
<h4> Dodaj nov recept </h4>
<form action="/dodaj/" method="POST">
    <h6> Naslov recepta: </h6> <input type="text" name="naslov_recepta" class="mb-1" required> <br>
    <div class="row mt-3"> </div>
    <h6> Čas priprave: </h6> <input type="time" min="00:05" max="5:59" required name="cas_priprave"  class="mb-1"> <br>
    <div class="row mt-3"></div>
    <h6> Kalorijska vrednost: </h6> <input type="text" name="kalorijska_vrednost" placeholder="zapiši s številom" class="mb-1" required> kal <br>
    <div class="row mt-3"></div>
    <h6> Slika: </h6> <input type="text" name="povezava_slike" placeholder="pripni povezavo" class="mb-1" required> <br>
    <div class="row mt-3"></div>
    <h6> Seznam sestavin: </h6> <textarea rows="10" cols="50" name="seznam_sestavin" placeholder="vsako sestavino podaj v svoji vrstici" class="mb-1" required> </textarea> <br>
    <div class="row mt-3"> </div>
    <h6> Navodila: </h6> <textarea rows="10" cols="50" name="navodila" class="mb-1" required> </textarea> <br>
    <input type="submit" class="btn btn-secondary btn-sm" value="Dodaj" >
</form>


 
 