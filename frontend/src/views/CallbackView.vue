<template>
    <div>
      <h1>Callback received</h1>
      <p>Status: {{ status }}</p>
      <p>Transaction ID: {{ transactionId }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        status: null,
        transactionId: null,
      };
    },
    mounted() {
      // Parse the URL parameters (query params)
      const urlParams = new URLSearchParams(window.location.search);
      this.status = urlParams.get('status');
      this.transactionId = urlParams.get('transaction_id');
  
      // Handle the data, e.g., make an API request to verify transaction, etc.
      if (this.status === 'success') {
        // You can call an API to verify or process the data here
        console.log('Transaction successful with ID:', this.transactionId);
      } else {
        console.log('Transaction failed');
      }
    },
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>
  