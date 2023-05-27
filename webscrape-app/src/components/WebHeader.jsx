import React from "react";
import '../App.css'
import img from "../assets/grocery.png"

export default function WebHeader(){
    return (
        <div className="nav">
            <img className='groceryPic' src={img} />
            <h1>Grocery Price Comparator</h1>
        </div>
    )
}