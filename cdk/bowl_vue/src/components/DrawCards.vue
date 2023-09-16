<script setup lang="ts">

import axios from 'axios'
import { useState, useActions, useGetters } from 'vuex-composition-helpers/dist'
const { drawCards } = useActions(['drawCards'])
const { token } = useState(['token'])

import Button from './Button.vue'
import ButtonGroup from './ButtonGroup.vue'

const discard = false;

const draw = async (numberOfCards) => {

    // first must make call to API to draw cards
    const api = axios.create({baseURL: 'https://q3a2yqmn16.execute-api.us-west-2.amazonaws.com'});

    const headers = {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token.value}`
    };
    const body = {'cards': numberOfCards};
    const reply = await api.post('/game/cards/draw', JSON.stringify(body), { headers });

    // put hand into state
    drawCards(reply.data.hand);
};

</script>

<template>
    <div class='draw-cards'>
        <div class='button-overlay'>
            <Button text='Discard' v-show="discard" />
            <Button text='Spare' @click.once="draw(1)" />
            <Button text='Strike' @click.once="draw(2)" />
            <ButtonGroup>
                <Button text='+3' @click.once="draw(3)" />
                <Button text='+4' @click.once="draw(4)" />
                <Button text='+6' @click.once="draw(6)" />
                <Button text='Finish' />
            </ButtonGroup>
        </div>
    </div>
</template>

<style scoped>

.draw-cards {
    position: fixed;
    bottom: 0.5em;
    width: 90%;
    left: 50%;
    margin-left: -45%;
    z-index: 1000;
}
  
.draw-cards .button-overlay {
      
    display: table;
    margin: 0 auto;
}

.draw-cards .button-overlay ul.button-group {
    list-style: none;   
}

</style>
