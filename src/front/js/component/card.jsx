import React from "react";
import "../../styles/cards.css";


const Card = ({name, image}) => {
    return (
		<div className="col col-md-3">
			<div className="card border-0 mx-auto bg-dark" style={{width: "350px", cursor: 'pointer'}}>
				<img src={image} className="card-img-top" style={{height: '150px'}} alt={name}/>
				<div className="card-body">
					<h5 className="card-title text-white mt-2">{name}</h5>
					<div className="overlay">
						<a href="#" className="btn btn-warning mt-2 read-more">Read more!</a>
					</div>
  				</div>
			</div>
		</div>
	)
}

export default Card