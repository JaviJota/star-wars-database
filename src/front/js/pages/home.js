import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";
import "../../styles/cards.css";
import Card from "/workspaces/star-wars-database/src/front/js/component/card.jsx"

export const Home = () => {
	const { store, actions } = useContext(Context);
	return (
		<div className="mt-5">
			<div className="row">
				{store.people?.map((person, index) => (
					<Card key={index} name={person.name} image={store.peopleImages[index]}/>
				))}
			</div>
		</div>
	);
};
