<template>
    <div class="header">
        <span>
            <button :disabled='!display.getGameLeft'>&lt;&lt;</button>
        </span>&nbsp;|&nbsp; 
        <span>
            <button :disabled='leftFrameDisabled' @click='prevFrame'>Previous Frame</button>
        </span>&nbsp;|&nbsp; 
        <span>
            <button :disabled='rightFrameDisabled' @click='nextFrame'>Next Frame</button>
        </span>&nbsp;|&nbsp; 
        <span>
            <button :disabled='!display.getGameRight'>&gt;&gt;</button>
        </span>
    </div>
    <div class='scoreboard'>
        <span class='frame'>Frame {{ display.getFrameNumber }}</span>
        <div class='score'>

            <table class='box'>
                <tbody>
                    <tr>
                        <td v-for="t, i in display.getFrameThrows.value" :class="i > 0 ? 'box' : 'none'">
                            {{ t }}
                        </td>
                    </tr>
                    <tr>
                        <td colspan='display.getFrameNumber.value === 10 ? 3 : 2'>
                            {{ display.getFrameScore }}
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    <div>
        <div class='flippable'i @click='checkMe'>
            <template v-for='url in display.getAnalysis.value'>
                <img :src="url" height="600" width="140" />
            </template>
        </div>
    </div>


    <div class='collapsed-panel' @click='togglePanel'>
        Open Me
    </div>
    <div class='slide-up-panel'>
        <transition name='slide-up'>
            <div v-if='display.getSliderIsOpen.value' class='slide-up-panel'>
                <div class='panel-content'>
                    <h1>Enter data</h1>
                    <div class='pins'>
                        <template v-for='(p, i) in [7,8,9,10]'>
                            <template v-if='i > 0'>&nbsp;&nbsp;&nbsp;</template>
                            <span @click='clickPins(p)' :class='pinsClassname(p)'>{{p}}</span>
                        </template>
                        <br />

                        <template v-for='(p, i) in [4, 5, 6]'>
                            <template v-if='i > 0'>&nbsp;&nbsp;&nbsp;</template>
                            <span @click='clickPins(p)' :class='pinsClassname(p)'>{{p}}</span>
                        </template>
                        <br />

                        <template v-for='(p, i) in [2, 3]'>
                            <template v-if='i > 0'>&nbsp;&nbsp;&nbsp;</template>
                            <span @click='clickPins(p)' :class='pinsClassname(p)'>{{p}}</span>
                        </template>
                        <br />

                        <template v-for='(p, i) in [1]'>
                            <span @click='clickPins(p)' :class='pinsClassname(p)'>{{p}}</span>
                        </template>

                    </div>
                    <div>
                        <label for="pins">Pins</label><input v-model='pinsBinding' /><br /><button @click='usePins'>Use Pins</button> <button @click='spare'>Spare</button> <button @click='strike'>Strike</button>
                    </div>
                    <div class="analysisInput">
                        <label class="left">Pin Exit</label>
                        <input name="pinExit" />
                        <input name="arrows" />
                        <label>Arrows</label>
                        <br style="clear: both" />
                        <label class="left">Pin Enter</label>
                        <input name="pinEnter" />
                        <input name="slide" />
                        <label>Slide</label>
                        <br style="clear: both" />
                        <label class="left">Break Pt.</label>
                        <input name="breakPoint" />
                        <input name="start" />
                        <label>Start</label>
                        <br style="clear: both" />
                        <label class="left">Break Dist.</label>
                        <input name="breakPoint" />
                        <br style="clear: both" />
                    </div>
            
                    <div class='submit'>
                        <button>Submit</button>&nbsp;&nbsp;&nbsp;<button @click='togglePanel'>Close Me</button>
                    </div>
                </div>
            </div>
        </transition>
    </div>

</template>

<style>

    .header button {
        height: 30px;
    }
    
    div.header {
        margin-bottom: 10px;
    }

    table.box td {
        height: 25px;
        width: 25px;

    }
    .pins {
        line-height: 60px
    }

    .pins span {
        padding: 15px;
        cursor: pointer;
    }

    .pins .yes {
        background-color: green
     }

    .pins .no {
        background-color: gray
    }

    div.analysisInput {
        height: 200px;
    }

    div.submit {
        height: 100px;
    }

    .analysisInput label {
        display: block;
        width: 60px;
        margin-left: 10px;
        margin-right: 0px;
        float: left;
    }

    .analysisInput label.left {
        text-align: right;
        margin-right: 10px;
        margin-left: 0px;
    }

    .analysisInput input {
        display: block;
        width: 70px;
        float: left;
        height: 40px;
    }

    .scoreboard {
        display: block;
        height: 75px;
    }

    .scoreboard .frame {
        float: left;
        margin-right: 30px;
    }
    .scoreboard .score {
        float: left;
    }

    .box {
        border: 1px solid;
    }

    div.flippable {
        background-color: yellow;
        height: 600px;
        width: 140px;
    }

    .collapsed-panel {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
    }

    .slide-up-panel {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #cccccc;
        border-top: 1px solid #000;
        box-shadow: 0px -2px 5px rgba(0, 0, 0, 0.2);
        z-index: 1000;
    }

    .panel-content {
        padding: 0px 20px 20px 40px;
        display: block;
    }

    .slide-up-enter-active,
    .slide-up-leave-active {
        transition: transform 0.3s ease;
    }

    .slide-up-enter,
    .slide-up-leave-to {
        transform: translateY(100%);
    }
</style>

<script setup>
    import { storeToRefs } from 'pinia';
    import { useDisplayStore } from '../stores/display';
    import { useAnalysisStore } from '../stores/analysis';
    import { computed, ref } from 'vue';
    
    const displayStore = useDisplayStore();
    const display = storeToRefs(displayStore);

    const analysisStore = useAnalysisStore();
    const analysis = storeToRefs(analysisStore);

    //const frames = display.getMaster.value.gameData[display.getGameNumber.value].frames;
    //const fs = frames.map((e) => e.frameNumber);
    //console.log(fs);
    //.map((e) => e.frameNumber)
    //console.log(`${display.getFrameNumber} :: ${frames}`);
    //console.log(display.getMaster.value.gameData[display.getFrameNumber.value].frames);
    //console.log(display.getGameLeft.value)
    //console.log(display.getFrameLeft.value)
    //console.log(display.getFrameRight.value)

    const togglePanel = () => {
        displayStore.toggleSlider();
    };

    const nextFrame = () => {
        displayStore.nextFrame();
    };

    const prevFrame = () => {
        displayStore.previousFrame();
    };

    const clickPins = (p) => {
        analysisStore.pins(p);
    };
    const pinsClassname = (p) => {
        return analysis.getPinsClicked.value.has(p) ? 'yes' : 'no';
    };
    const spare = () => {
        analysisStore.spare();
    };
    const strike = () => {
        analysisStore.strike();
    };

    const checkMe = () => {
        console.log(display.getAnalysis.value);
    };

    const analysisImages = () => {
        return display.getAnalysis.value;
    };

    const usePins = () => {
        console.log('usingPins');
        analysisStore.usePins();
    };

    const pinsBinding = computed({
        get() {
            return analysisStore.pinsText;
        },
        set(value) {
            console.log(`setting...${value}`);
            analysisStore.pinText(value);
        }
    });

    const leftFrameDisabled = computed({
        get() {
            return display.getFrameNumber.value === 1
        }
    });
    const rightFrameDisabled = computed({
        get() {
            return display.getFrameNumber.value === Math.max(...display.getTotalFrames.value);
        }
    });

</script>
