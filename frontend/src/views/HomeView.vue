<template>
  <h2 class="text-xl font-bold">Ödeme Formu</h2>

  <div class="home flex m-auto gap-2 relative">
    <fieldset class="fieldset w-xs bg-gray-750 border border-gray-400 font-semibold text-white p-4 rounded-box">
      <legend class="fieldset-legend text-white">Ürünleriniz</legend>
      
    </fieldset>

    <fieldset class="fieldset w-xs bg-gray-750 border border-gray-400 font-semibold text-white p-4 rounded-box">
      <legend class="fieldset-legend text-white">Alıcı Adresi</legend>
      
      <div class="flex gap-2">
        <div>
          <label class="fieldset-label text-white">Alıcı Adı</label>
          <input type="text" class="input" placeholder="Name" />
        </div>
        <div>
          <label class="fieldset-label text-white">Alıcı Soyadı</label>
          <input type="text" class="input" placeholder="Name" />
        </div>
      </div>
      
      <label class="fieldset-label text-white">Adres adı <span class="text-gray-500">(Optional)</span></label>
      <input type="text" class="input" placeholder="My awesome page" />
      
      <label class="fieldset-label text-white">Ülke</label>
      <input type="text" class="input" placeholder="my-awesome-page" />
       
      <label class="fieldset-label text-white">şehir</label>
      <input type="text" class="input" placeholder="my-awesome-page" />      
      
      <label class="fieldset-label text-white">ilçe</label>
      <input type="text" class="input" placeholder="my-awesome-page" />

      <label class="fieldset-label text-white">posta kodu</label>
      <input type="text" class="input" placeholder="my-awesome-page" />
      
      <legend class="fieldset-legend text-white">Adresiniz</legend>
      <textarea class="textarea h-24" placeholder="Bio"></textarea>
    </fieldset>

    <fieldset class="fieldset w-xs bg-gray-750 border border-gray-400 font-semibold text-white p-4 rounded-box">
      <legend class="fieldset-legend text-white">Ödeme bilgileri</legend>
      
    </fieldset>

    <div class="absolute right-0 -bottom-14 ">
      <button class="btn btn-primary">Ödeme Yap</button>
    </div>
</div>
</template>

<script setup>

</script>
