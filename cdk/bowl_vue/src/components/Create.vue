<script setup lang="ts">

import axios from 'axios'
import { Buffer } from 'buffer' 
import { useActions } from 'vuex-composition-helpers/dist'
const { changeView, storeGameInfo } = useActions(['changeView', 'storeGameInfo'])

import Button from './Button.vue'

let playerName = '';

const createGame = async () => {

    // first must make call to API to create the game
    const api = axios.create({baseURL: 'https://q3a2yqmn16.execute-api.us-west-2.amazonaws.com'});

    const headers = {
        'Content-Type': 'application/json'
    };
    const body = {
        playerName,
        decks: 1
    };
    const reply = await api.post('/game/create', JSON.stringify(body), { headers });

    console.log(reply.data.token);

    const payload = JSON.parse(Buffer.from(reply.data.token.split('.')[1], 'base64').toString());

    const gameId = payload.sub.split(' ')[0];
    const playerId = payload.sub.split(' ')[1];

    // then put the game info into state
    storeGameInfo({playerName, token: reply.data.token, gameId, playerId, isHost: true});

    // then change state to Pregame
    changeView('Pregame');
};

</script>

<template>
    <div class='create-game'>
        <div class='grid-x row align-center'>
            <div class='column'>
                <input type='text' v-model='playerName'  placeholder='Enter Your Name' />
            </div>
        </div>
        <div class='grid-x row align-center'>
            <div class='column'>
                <Button text='Play Now!' @click.once="createGame" />
            </div>
        </div>
    </div>
</template>

<style scoped>

.create-game {
    
    position: absolute;
    top: 50%;
    left: 50%;
    -ms-transform: translateX(-50%) translateY(-50%);
    -webkit-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    width: 100%;   
}

.create-game .draw-button {    
    float: none;
    margin-right: 0;
	font-size: 3em;
	margin-top: 0.5em;
    margin-bottom: 0.5em;
}

</style>
