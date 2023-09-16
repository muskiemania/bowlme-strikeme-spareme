<script setup lang="ts">

import axios from 'axios'
import Button from './Button.vue'

import { useState, useActions, useGetters } from 'vuex-composition-helpers/dist'
const { changeView } = useActions(['changeView'])
const { token } = useState(['token']);


const startGame = async () => {

    console.log(`start token: ${token.value}`);
    // first must make call to API to create the game
    const api = axios.create({baseURL: 'https://q3a2yqmn16.execute-api.us-west-2.amazonaws.com'});

    const headers = {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token.value}`
    };
    const body = { status: 'start' };
    await api.post('/game/status', JSON.stringify(body), { headers });

    // then change state to Pregame
    changeView('PokerGame');
};
</script>

<template>
    <div class='pregame'>
        <div class='button-overlay'>
            <Button text='Waiting...' @touch="startGame" @mouseup="startGame" />
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
}
  
.pregame .button-overlay {
    display: table;
    margin: 0 auto;
}

.pregame .button-overlay ul.button-group {
    list-style: none;   
}

.pregame .draw-button {  
    margin-right: 0;
}

</style>
