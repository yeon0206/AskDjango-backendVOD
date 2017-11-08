import re
from django import forms
from django.template.loader import render_to_string
# from askdjango import settings (x)
from django.conf import settings
# => (django/conf/global_settings.py + askdjango/settings.py)

class NaverMapPointWidget(forms.TextInput):
    BASE_LAT, BASE_LNG = '37.497921', '127.027636' # 강남역
    def render(self, name, value, attrs):
        width = str(self.attrs.get('width', 800))
        height = str(self.attrs.get('height', 600))
        if width.isdigit(): width += 'px'
        if height.isdigit(): height += 'px'

        ctx={
            'naver_client_id' : settings.NAVER_CLIENT_ID,
            'id' : attrs['id'],
            'width': width,
            'height' : height,
            'base_lat': self.BASE_LAT, 
            'base_lng': self.BASE_LNG,
        }
        
        #수정 들어갔을 때, 저장한 경도위도에 깃발이 표시되도록
        if value:
            try:
                lng, lat = re.findall(r'[+-]?[\d\.]+', value)
                ctx.update({'base_lat': lat, 'base_lng': lng})
            except (IndexError, ValueError):
                pass
        html=render_to_string('widgets/naver_map_point_widget.html', ctx)
        
        attrs['readonly'] = 'readonly' #사용자가 직접입력못하도록
        parent_html = super().render(name,value,attrs)

        return parent_html + html