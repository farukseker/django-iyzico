<template>
  <h2 class="text-xl font-bold">Ödeme Formu</h2>
  <!-- <div
  v-if="show_form"
  class="absolute flex w-full min-h-screen z-40 bg-gray-800 bg-opacity-50 top-0 left-0"
  >
    <iframe
      class="m-auto w-[400px] h-[600px] border"
      ref="form_3d"
      href="http://localhost:8080/"
      @load="handleIframeLoad"
      referrerpolicy="
        origin
        origin-when-cross-origin
        same-origin
        strict-origin
        strict-origin-when-cross-origin
        unsafe-url
      "
      sandbox="allow-scripts allow-forms allow-same-origin"
      ></iframe>
  </div>   -->
  <fieldset class="fieldset w-xs bg-gray-750 border border-gray-400 font-semibold text-white p-4 rounded-box z-30">
    <legend class="fieldset-legend text-white">Oturum Yardımcısı</legend>
    <div class="flex gap-2">
      <button class="btn btn-primary" @click="login">Giriş Yap</button>
      <button class="btn btn-primary" @click="logout"> Çıkış Yap</button>
      <button class="btn btn-error " @click="get_installment_info"> Taksit bilgisi Al</button>
    </div>
  </fieldset>

  <article class="absolute w-full h-full flex">
    <div class="home flex m-auto gap-2 relative">
    <div class="gap-2 flex-wrap h-full">
      <fieldset class="h-80 fieldset w-xs bg-gray-750 border border-gray-400 font-semibold text-white p-4 rounded-box">
        <legend class="fieldset-legend text-white">Ürünleriniz</legend>
          <div class="overflow-x-auto rounded-box border border-base-content/5 bg-base-100">
            <table class="table table-sm text-sm text-gray-900">
              <!-- head -->
              <thead>
                <tr>
                  <th></th>
                  <th>Adı</th>
                  <th>Kategori</th>
                  <th>Add</th>
                </tr>
              </thead>
              <tbody>
                <!-- row 1 -->
                <tr v-for="(product, index) in product_list" v-bind:key="index">
                  <th>{{ index }}</th>
                  <td>{{ product.name }}</td>
                  <td>{{ product.category }}</td>
                  <td>
                    <button class="btn btn-success btn-sm" @click="basket.push(product)">add</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
      </fieldset>
    
      <fieldset class="h-80 fieldset w-xs bg-gray-750 border border-gray-400 font-semibold text-white p-4 rounded-box">
        <legend class="fieldset-legend text-white">Sepet</legend>
        <div class="overflow-x-auto rounded-box border border-base-content/5 bg-base-100">
        
        <table class="table table-sm text-sm text-gray-900">
              <!-- head -->
              <thead>
                <tr>
                  <th></th>
                  <th>Adı</th>
                  <th>Kategori</th>
                  <th>RM</th>
                </tr>
              </thead>
              <tbody>
                <!-- row 1 -->
                <tr v-for="(product, index) in basket" v-bind:key="index">
                  <th>{{ index }}</th>
                  <td>{{ product.name }}</td>
                  <td>{{ product.category }}</td>
                  <td>
                    <button class="btn btn-error btn-sm" @click="basket.splice(index, 1)">RM</button>
                  </td>
                </tr>
              </tbody>
            </table>
        </div>
      </fieldset>
    
    </div>

    <fieldset class="fieldset w-xs bg-gray-750 border border-gray-400 font-semibold p-4 rounded-box text-gray-900">
      <legend class="fieldset-legend text-white">Alıcı Adresi</legend>
      
      <div class="flex gap-2">
        <div>
          <label class="fieldset-label text-white">Alıcı Adı</label>
          <input type="text" class="input" placeholder="Name" v-model="address_data.name" />
        </div>
        <div>
          <label class="fieldset-label text-white">Alıcı Soyadı</label>
          <input type="text" class="input" placeholder="Surname" v-model="address_data.surname" />
        </div>
      </div>
      
      <label class="fieldset-label text-white">Adres adı <span class="text-gray-500">(Optional)</span></label>
      <input type="text" class="input" placeholder="Title" v-model="address_data.title" />
      
      <label class="fieldset-label text-white">Ülke</label>
      <input type="text" class="input" placeholder="Country" v-model="address_data.country" />
       
      <label class="fieldset-label text-white">şehir</label>
      <input type="text" class="input" placeholder="City" v-model="address_data.city"/>      
      
      <label class="fieldset-label text-white">ilçe</label>
      <input type="text" class="input" placeholder="District" v-model="address_data.district" />

      <label class="fieldset-label text-white">posta kodu</label>
      <input type="text" class="input" placeholder="Post Code" v-model="address_data.postCode" />
      
      <legend class="fieldset-legend text-white">Adresiniz</legend>
      <textarea class="textarea h-24" placeholder="Address" v-model="address_data.address"></textarea>
    </fieldset>

    <fieldset class="fieldset w-xs bg-gray-750 border border-gray-400 font-semibold text-gray-900 p-4 rounded-box">
      <legend class="fieldset-legend text-white">Ödeme bilgileri</legend>
        <label class="fieldset-label text-white">Kıredi Kartı Sahibi Adı</label>
        <input type="text" class="input" placeholder="City" v-model="credit_card_info.fullName"/>      
        
        <label class="fieldset-label text-white">Kıredi Kartı No</label>
        <input type="text" class="input" placeholder="District" v-model="credit_card_info.creditCardNumber" />

        <fieldset class="fieldset w-xs bg-gray-750 border border-gray-400 font-semibold text-gray-900 p-4 rounded-box">
          <legend class="fieldset-legend text-white">Son kullanma bilgileri</legend>
          <div class="flex gap-2">
            <div>
              <label class="fieldset-label text-white">Son kullanma Ay</label>
              <input type="text" class="input" placeholder="Name" v-model="credit_card_info.creditCardExpiryMonth" />
            </div>
            <div>
              <label class="fieldset-label text-white">Son kullanma Yıl</label>
              <input type="text" class="input" placeholder="Name" v-model="credit_card_info.creditCardExpiryYear" />
            </div>
          </div>
        </fieldset>
        <div>
          <label class="fieldset-label text-white">CVC Kodu</label>
          <input type="text" class="input" placeholder="Surname" v-model="credit_card_info.creditCardCVC" />
        </div>

      <div class="w-full flex gap-2">
        <input id="is3d" type="checkbox" class="checkbox checkbox-primary" placeholder="Surname" v-model="credit_card_info.is3d" />
        <label for="is3d" class="fieldset-label text-white">3d Ödeme Yap</label>
      </div>
        <button class="btn btn-primary" @click="pay">Ödeme Yap</button>
      </fieldset>
    </div>
  </article>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import api from "@/utils/axios";


const citys = ref([])

const laod_citys = async () => {
  const response = await fetch('/data/citys.json')
  if (response.ok){
    citys.value = await response.json()
  }
}

const login = () => {
  api.post("/user/token", {
    username: "pars",
    password: "pars"
  })
  .then(response => localStorage.setItem("token", response.data.access))
  .catch(error => console.error(error));
}

const logout = () => {localStorage.removeItem("token")}


const product_list = ref([])

const load_product_list = () => {
  api.get("/product/")
  .then(response => product_list.value = response.data)
  .catch(error => console.error(error));
}

const basket = ref([])

const address_data = ref({
  name: "Faruk",
  surname: "Şeker",
  title: null,
  country: 'Türkiye',
  city: 'Izmir',
  district: 'Karşıyaka',
  postCode: '35320',
  address: 'kebab'
}) 

const credit_card_info = ref({
  fullName: 'Faruk Şeker',
  creditCardNumber: '5890040000000016',
  creditCardExpiryMonth: '6',
  creditCardExpiryYear: '2026',
  creditCardCVC: '123',
  is3d: true,
  isSave: false,
})

// const checkout_url = ref('')

const pay = () => {
  const api_request = {
    credit_card_info: credit_card_info.value,
    address_info: address_data.value,
    basket: basket.value
  }
  
  api.post("/payment", api_request)
  
  .then(response => {
    // show_form.value = true
    // checkout_url.value = response.data.checkout_url
    window.location.href = response.data.checkout_url;

    // router.push(response.data.checkout_url)
    // nextTick(
    //   renderHtml(response.data.form_3d)
    // )
  })
  .catch(error => console.error(error));
}

const get_installment_info = () => {
  api.post("/installment", {
    binNumber: credit_card_info.value.creditCardNumber.slice(0, 8),
    price: 405
  })
  .then(response => {
    console.log(response)
    console.log(response.data)
  })
  .catch(error => console.error(error));
}

onMounted(()=> {
  load_product_list();
  laod_citys();
})

</script>
