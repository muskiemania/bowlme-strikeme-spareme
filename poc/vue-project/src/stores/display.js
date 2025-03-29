import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useDisplayStore = defineStore('display', {

    state: () => {
        return {
            gameNumber: 1,
            //frameLeft: ref(false),
            //frameRight: ref(false),
            frameNumber: 1,
            //throw1: ref(0),
            //throw2: ref(0),
            //throw3: ref(0),
            analysisCursor: ref(0),
            analysis1: ref(''),
            analysis2: ref(''),
            analysis3: ref(''),
            master: ref({
                games: [1,2,3],
                gameData: {
                    "1": {
                        "frames": [
                            {
                                "frameNumber": 1,
                                "throws": [
                                    {
                                        "pins": "7"
                                    },
                                    {
                                        "pins": "/"
                                    }
                                ],
                                "totalScore": 18
                            },
                            {
                                "frameNumber": 2,
                                "throws": [
                                    {
                                        "pins": "8"
                                    },
                                    {
                                        "pins": "1"
                                    }
                                ],
                                "totalScore": 27
                            },
                        ]
                    },
                    "2": {
                    },
                    "3": {
                    }
                }
            })
        };
    },
    getters: {
    
        getGameNumber: (state) => state.gameNumber,
        getGameLeft: (state) => state.gameNumber > 1,
        getGameRight: (state) => state.gameNumber === Math.max(state.master.games),
        getFrameNumber: (state) => state.frameNumber,
        getFrameLeft: (state) => state.frameNumber > 1,
        getFrameRight: (state) => {
            const frames = state.master.gameData[state.gameNumber.toString()].frames.map((e) => e.frameNumber)
            console.log(`${state.frameNumber} :: ${frames}`);
            return state.frameNumber === Math.max(frames);
        },
        getFrameThrows: (state) => {
            const f = state.master.gameData[state.gameNumber.toString()].frames.find((e) => e.frameNumber === state.frameNumber);
            return f['throws'].map((e) => e['pins']);
        },
        getFrameScore: (state) => {
            const f = state.master.gameData[state.gameNumber.toString()].frames.find((e) => e.frameNumber === state.frameNumber);
            return f.totalScore
        },
        getMaster: (state) => state.master
    },
    actions: {

    }
});

