import React from "react";
import { Link } from "react-router-dom";
import data from "./data";
import "./CategoryList.css";

const CategoryList = () => {
  return (
    <div className="categories">
      <h2>Список категорий</h2>
      <ul>
        {data.categories.map((category) => (
          <li key={category.id}>
            <Link to={`/recipes/${category.id}`}>{category.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CategoryList;
