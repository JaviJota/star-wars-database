const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			people: [],
			planets: [],
			starships: [],
			token: '',
			user: '',
			peopleImages: [
				"https://lumiere-a.akamaihd.net/v1/images/luke-skywalker-main_7ffe21c7.jpeg?region=270%2C143%2C1070%2C804",

			],
			message: null,
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			]
		},
		actions: {
			getPeople: async () => {
				try {
					const resp = await fetch('https://swapi.dev/api/people');
					const data = await resp.json();
					if(!resp.ok) throw new Error('Error retrieving people');
					setStore({ people: data.results})
					localStorage.setItem('people', JSON.stringify(data.results));
					return true
				} catch (error) {
					console.log('Error retrieving people', error)
				}
			},
			getPlanets: async () => {
				try {
					const resp = await fetch('https://swapi.dev/api/planets');
					const data = await resp.json();
					if(!resp.ok) throw new Error('Error retrieving planets');
					setStore({ planets: data.results})
					localStorage.setItem('planets', JSON.stringify(data.results))
					return true
				} catch (error) {
					console.log('Error retrieving planets', error)
				}
			},
			getStarships: async () => {
				try {
					const resp = await fetch('https://swapi.dev/api/starships');
					const data = await resp.json();
					if(!resp.ok) throw new Error('Error retrieving starships');
					setStore({ starships: data.results})
					localStorage.setItem('starships', JSON.stringify(data.results))
					return true
				} catch (error) {
					console.log('Error retrieving starships, error')
				}
			},
			// Use getActions to call a function within a fuction
			exampleFunction: () => {
				getActions().changeColor(0, "green");
			},

			getMessage: async () => {
				try{
					// fetching data from the backend
					const resp = await fetch(process.env.BACKEND_URL + "api/hello")
					const data = await resp.json()
					setStore({ message: data.message })
					// don't forget to return something, that is how the async resolves
					return data;
				}catch(error){
					console.log("Error loading message from backend", error)
				}
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			}
		}
	};
};

export default getState;
