<script setup lang="ts">

import Button from './Button.vue'

import { useState, useActions, useGetters } from 'vuex-composition-helpers/dist'
const { changeView } = useActions(['changeView'])
const { mode } = useState(['mode']);

console.log(mode);

</script>

<template>
    <div class='pregame'>
        <div class='button-overlay'>
            <Button text='Waiting...' @click="changeView('PokerGame')" />
        </div>
    </div>
</template>

<style scoped>
.pregame {
    position: fixed;
    bottom: 0.5em;
    width: 90%;
    left: 50%;
    margin-left: -45%;
    z-index: 1000;
  
    .button-overlay {
      
        display: table;
        margin: 0 auto;
    
        ul.button-group {
	        list-style: none;   
        }
    }
  
    .draw-button {
        margin-right: 0;
    }
}

</style>
