const renderProduct = ({id, name, description, cost, image}) => (
    `
        <div class="products__item">
            
            <img 
                class="products__item-image"
                src="${ image ? image : '/static/products/images/empty.png' }"
                alt="${ name }"
            >
            <span class="products__item-name">
                ${ name }
            </span>
            <span class="products__item-description">
                ${ description }
            </span>
            <span class="products__item-cost">
                ${ cost ? cost : 'Значение отсутствует'}
            </span>
            <a href="/products/${ id }" class="products__item-link">
                Ссылка на ${ name }
            </a>
        </div>
    `
)