import React from "react";
import '../App.css'

export default function ResultItems(props){

    return(
        <div className="item-card">
            <h2>{props.title}</h2>
            <h4>Weight: </h4>
            <h4>Store: {props.store}</h4>
            <h4 className="price"><b>${props.price}</b></h4>
        </div>
    )
}