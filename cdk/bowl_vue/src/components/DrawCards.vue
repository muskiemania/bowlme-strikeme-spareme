<script setup lang="ts">

import axios from 'axios'
import { useState, useActions, useGetters } from 'vuex-composition-helpers/dist'
const { resetCards } = useActions(['resetCards'])
const { token, hand } = useState(['token', 'hand'])
const { canDiscard, canDraw } = useGetters(['canDiscard', 'canDraw']);

import Button from './Button.vue'
import ButtonGroup from './ButtonGroup.vue'

const sortCards = (cards) => {

    const cartesian = (a, b) => a.reduce((p, x) => [...p, ...b.map(y => `${x}${y}`)], []);
    const nums = ['2','3','4','5','6','7','8','9','T','J','Q','K','A'];
    const suits = ['C','D','H','S'];
    const deck = cartesian(nums, suits);
    
    return cards.sort((a, b) => { return deck.indexOf(a) - deck.indexOf(b); });
}

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
    resetCards(sortCards(reply.data.hand));
};

const discard = async () => {

    // first get the cards to discard (from store)
    const discard = hand.value.filter((card) => card.selected).map((card) => {
        return card.card;
    });

    // first must make call to API to draw cards
    const api = axios.create({baseURL: 'https://q3a2yqmn16.execute-api.us-west-2.amazonaws.com'});

    const headers = {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token.value}`
    };
    const body = { cards: discard };
    const reply = await api.post('/game/cards/discard', JSON.stringify(body), { headers });

    // put hand into state
    resetCards(sortCards(reply.data.hand));
};



</script>

<template>
    <div class='draw-cards'>
        <div class='button-overlay'>
            <Button text='Discard' v-show="canDiscard" @touch="discard" @mouseup="discard" />
            <Button text='Spare' @touch="draw(1)" @mouseup="draw(1)" v-show="canDraw" />
            <Button text='Strike' @touch="draw(2)" @mouseup="draw(2)" v-show="canDraw" />
            <ButtonGroup>
                <Button text='+3' @touch="draw(3)" @mouseup="draw(3)" v-show="canDraw" />
                <Button text='+4' @touch="draw(4)" @mouseup="draw(4)" v-show="canDraw" />
                <Button text='+6' @touch="draw(6)" @mouseup="draw(6)" v-show="canDraw" />
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
