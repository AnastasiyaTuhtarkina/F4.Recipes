import React from "react";
import { Link, useParams } from "react-router-dom";
import data from "./data";
import "./RecipeList.css";

const RecipeList = () => {
  const { categoryId } = useParams();
  const category = data.categories.find(
    (category) => category.id === categoryId
  );
  const categoryName = category ? category.name : "Неизвестная категория"; // Фолбек на случай если категория не найдена

  const recipes = data.recipes.filter(
    (recipe) => recipe.categoryId === categoryId
  );

  console.log("CategoryId:", categoryId);
  console.log("Recipes:", recipes);

  return (
    <div className="recipe-list">
      {" "}
      {/* Добавляем класс для стилей */}
      <h2>Рецепты для категории: {categoryName}</h2>
      {/* Отображение рецептов */}
      <ul>
        {recipes.map((recipe) => (
          <li key={recipe.id}>
            <Link to={`/recipe/${recipe.id}`}>{recipe.title}</Link>{" "}
            {/* Ссылка на страницу рецепта */}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RecipeList;
