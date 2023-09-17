<script setup lang="ts">

import axios from 'axios'
import { Buffer } from 'buffer'
import { useActions, useState } from 'vuex-composition-helpers/dist'
const { changeView, storeGameInfo } = useActions(['changeView', 'storeGameInfo']);
const { gameId } = useState(['gameId']);

import Button from './Button.vue'

let playerName = '';

const joinGame = async () => {

    // first must make call to API to create the game
    const api = axios.create({baseURL: 'https://q3a2yqmn16.execute-api.us-west-2.amazonaws.com'});

    const headers = {
        'Content-Type': 'application/json'
    };
    const body = {
        playerName,
        gameId: gameId?.value
    };
    const reply = await api.post('/game/join', JSON.stringify(body), { headers });

    const payload = JSON.parse(Buffer.from(reply.data.token.split('.')[1], 'base64').toString());

    const t_gameId = payload.sub.split(' ')[0];
    const t_playerId = payload.sub.split(' ')[1];

    // then put the game info into state
    storeGameInfo({playerName, token: reply.data.token, playerId: t_playerId, isHost: false});

    // then change state to Pregame
    changeView('Pregame');
};



</script>

<template>
    <div class='join-game'>
        <div class='grid-x row align-center'>
            <div class='column'>
                <input type='text' placeholder='Enter Your Name' />
            </div>
        </div>
        <div class='grid-x row align-center'>
            <div class='column'>
                <Button text='Join Game Now' @touch="joinGame" @mouseup="joinGame" />
            </div>
        </div>
    </div>
</template>

<style scoped>

.join-game {

    position: absolute;
    top: 50%;
    left: 50%;
    -ms-transform: translateX(-50%) translateY(-50%);
    -webkit-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    width: 100%;
}

.join-game .draw-button {    
    float: none;
    margin-right: 0;
	font-size: 3em;
}

</style>
