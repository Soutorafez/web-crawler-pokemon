import scrapy
import json

class PokemonSpider(scrapy.Spider):
	name = 'pokemon'

	# Inicio da request
	def start_requests(self):
		yield scrapy.Request(url = 'https://www.solosagrado.com.br/categorias/253/Single-Cards/pagina/1/view/vertical/ord/4/qtdview/36', callback = self.parse)
	

	# resposta da request
	def parse(self, response):
		arr = []
		url ='https://www.solosagrado.com.br'
		for item in response.css('li.m_right_10'):
			
			for card in response.css('div.product_item.m_left_0.specials.w_xs_full.col-lg-3.col-md-3.col-sm-3'):
				name = card.css('.color_dark.bold::text').extract_first()
				preco = card.css('span.bold::text').extract_first()
				link = card.css('a.d_block.relative.pp_wrap.m_bottom_10').xpath('@href').extract_first()
				img = card.css('img.tr_all_hover').xpath('@src').extract_first()

				arr.append({
					'name': name.strip(),
					'preco': preco.strip(),
					'link': url+link.strip(),
					'image': img.strip()
				})
		
		yield scrapy.Request(url = 'https://www.solosagrado.com.br'+str(item.css('a.color_dark').xpath('@href').extract_first()), callback = self.parse)


		with open('pokemons.json', 'wb') as f:
			json.dump(arr, f)