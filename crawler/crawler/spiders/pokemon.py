import scrapy
import json

class PokemonSpider(scrapy.Spider):
	name = 'pokemon'

	# Inicio da request
	def start_requests(self):
		yield scrapy.Request(url = 'https://www.solosagrado.com.br/categorias/253/Single-Cards/pagina/1/view/vertical/ord/2/qtdview/36', callback = self.parse)
	

	# resposta da request
	def parse(self, response):
		arr = []
		url ='https://www.solosagrado.com.br'
		
		for card in response.css('div.product_item.m_left_0.specials.w_xs_full.col-lg-3.col-md-3.col-sm-3'):
			name = card.css('.color_dark.bold::text').extract_first()
			preco = card.css('span.bold::text').extract_first()
			link = card.css('a.d_block.relative.pp_wrap.m_bottom_10').xpath('@href').extract_first()
			img = card.css('img.tr_all_hover').xpath('@src').extract_first()

			arr.append({
				'name': name.strip(),
				'preco': preco.strip(),
				'link': link.strip(),
				'image': img.strip()
				})

		with open('pokemons.json', 'wb') as f:
			json.dump(arr, f)

			#name = response.css('a.color_dark.bold::text').extract()
			#preco = response.css('span.bold::text').extract()
			#link = response.xpath('//a[@class="d_block relative pp_wrap m_bottom_10"]/@href').extract()
	
		#for lin in link:
		#linkCompleto = 'https://www.solosagrado.com.br'+lin
		

##color_dark bold

##span.bold 