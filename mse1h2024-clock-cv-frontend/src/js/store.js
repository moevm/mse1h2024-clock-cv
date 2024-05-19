import Vuex from 'vuex'


const store = new Vuex.Store({
    state: {
        result: 0,
        description: '',
        imageId: '',
        entry: false,
        userId: '',
        userName: '',
        randomHours: 0,
        randomMinutes: 0,
    }
})

export default store