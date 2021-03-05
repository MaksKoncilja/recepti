% rebase('bootstrap.tpl')
<h4>Dodaj nov recept</h4>
<form action="/dodaj/" method="POST">
    Naslov recepta: <input type="text" name="naslov_recepta" class="mb-1"><br>
    <div class="row mt-3"></div>
    Čas priprave: <input type="time" min="00:05" max="5:59" required name="cas_priprave"  class="mb-1"><br>
    <div class="row mt-3"></div>
    Kolorijska vrednost: <input type="text" name="kalorijska_vrednost" class="mb-1"> kal<br>
    <div class="row mt-3"></div>
    Seznam sestavin: <br> <textarea rows="10" cols="50" name="seznam_sestavin" placeholder="vsako sestavino podaj v svoji vrstici" class="mb-1"></textarea><br>
    <div class="row mt-3"></div>
    Navodila: <br> <textarea rows="10" cols="50" name="navodila" class="mb-1"></textarea><br>
    <input type="submit" class="btn btn-secondary btn-sm" value="Dodaj">
</form>

 